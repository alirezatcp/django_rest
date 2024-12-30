from django.shortcuts import render

from django.db import transaction
# about asyncs:

from django.http import HttpResponse

from .models import Person

import asyncio
from asgiref.sync import sync_to_async, async_to_sync


# this is a sync view (all ORM is sync):
def get_person(request, first_name):
    person = Person.objects.get(first_name=first_name)
    return HttpResponse(f'person: {person}')


# this is async view (in async if something went wrong, it does another things and dont wait to end that first and it make works faster.):
async def wait_2_seconds(request):
    await asyncio.sleep(2)
    return HttpResponse('Hi')


# convert sync to async:
async def get_person1(request, first_name):

    # with using transaction.atomic() we see all queries inside that as one query and if one of them failed, like all of them failed.
    with transaction.atomic():
        # multi line
        person_get = sync_to_async(Person.objects.get)
        person = await person_get(first_name=first_name)

        # one line
        person = await sync_to_async(Person.objects.get)(first_name=first_name)

    return HttpResponse(f'person: {person}')


# or we can do it like this:
@sync_to_async
def person_get(first_name):
    return Person.objects.get(first_name=first_name)

async def get_person2(request, first_name):
    person = await person_get(first_name=first_name)
    return HttpResponse(f'person: {person}')


# use async as sync
@async_to_sync
async def hello_message(name):
    await asyncio.sleep(3)
    return f'welcome {name}'

def main():
    msg = hello_message('mohammad')
    print(msg)
