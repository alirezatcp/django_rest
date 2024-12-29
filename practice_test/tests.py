from django.test import TestCase

from practice_test.models import Person

import datetime

from model_bakery import baker # fills all fields of model that we didnt gave. install: pip install model_bakery


class PersonTests(TestCase):

    fixtures = ['person.json']
    
    def setUp(self):
        print(Person.objects.get(first_name='Alireza'))
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


class ViewTests(TestCase):
    # test a django view login
    def test_login(self):
        data = {'username': 'ali', 'password': '123'}
        response = self.client.post('/login/', data=data)
        self.assertEqual(response.status_code, 200)
    
    # test a django view
    def test_homepage(self):
        response = self.client.get('/homepage/')
        self.assertTrue(b'Welcome to the homepage' in response.content) # response.content returns binary so we used b''


class APIViewTests(TestCase):
    # a welcome page that returns: {'message': 'welcome to our site.'}
    def test_welcome(self):
        response = self.client.get('/welcome/')
        data = response.json()
        self.assertEqual(data.get('message'), 'welcome to our site.')

    # an string welcome page that returns: 'welcome to our site'
    def test_string_welcome(self):
        response = self.client.get('/string_welcome/')
        string_data = response.content.decode('utf-8')
        self.assertEqual('welcome to our site', string_data)


# testing code coverage:
# to install:
# pip install coverage
# to get coverage value:
# coverage run --source='.' manage.py test {app_name}
# to see result:
# coverage report
# to see result as html (after this command run htmlcov/index.html in browser to see results.):
# coverage html


# Fixtures
# we can use fixtures to add objects to our model.
# fixtures is json, xml or yaml files.
# we can use them in tests or add them to database.
# an example from fixtures is in practice_test/fixtures/person.json (if we change fixtures name we should change FIXTURE_DIRS in settings.py):
# we added our fixtures in PersonTests.
# to add fixtures to our database: python manage.py loaddata practice_test/fixtures/person.json
# to create fixture from our database:  python manage.py dumpdata > practice_test/fixtures/dumped_data.json
# or we can dump a table data:  python manage.py dumpdata table_name > practice_test/fixtures/dumped_data.json
# or we can dump an app data:  python manage.py dumpdata app_name > practice_test/fixtures/dumped_data.json