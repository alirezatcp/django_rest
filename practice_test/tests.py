from django.test import TestCase

from practice_test.models import Person

import datetime

from model_bakery import baker # fills all fields of model that we didnt gave. install: pip install model_bakery


class PersonTests(TestCase):
    def setUp(self):
        self.person = baker.make(Person, first_name='Firstname') # create an object from person that filled fields randomly.
        print(f'First name: {self.person.first_name}\nLast name: {self.person.last_name}\nBirth date {self.person.birth_date}') # show person detail
        Person.objects.create(first_name='Ali', last_name='Taghipour', birth_date= datetime.date(2000, 4, 12))
        Person.objects.create(first_name='Maryam', last_name='Nouri', birth_date= datetime.date(1956, 11, 10))

    def test_is_young(self):
        ali = Person.objects.get(first_name='Ali')
        maryam = Person.objects.get(first_name='Maryam')
        self.assertTrue(ali.is_young())
        self.assertFalse(maryam.is_young())
        # assertEqual, assertNotIn, assertIn

    def test_is_old(self):
        ali = Person.objects.get(first_name='Ali')
        maryam = Person.objects.get(first_name='Maryam')
        self.assertFalse(ali.is_old())
        self.assertTrue(maryam.is_old())

# we start testing all tests with this command: python manage.py test
# we start testing files in a directory tests with this command: python manage.py test directory
# we start testing a file we gave: python manage.py test app_name.test_file_name
# start test that have their own patterns: python manage.py test --pattern="pattern"
# start test a class: python manage.py test "class_name"
# start test a method: python manage.py test "method_name"