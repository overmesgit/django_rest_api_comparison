import json
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from resources.models import Entry


JSON_TYPE = 'application/json'


class ApiTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='first')

        self.entry1_args = {'user': self.user1, 'title': 'some name', 'content': 'some entry'}
        self.entry1 = Entry.objects.create(user=self.user1, title='some name', content='some entry')
        self.entry1_args['created_date'] = self.entry1.created_date

        self.entry_list_uri = None
        self.entry_detail_uri = None
        self.user_detail_uri = None

        self.c = Client()

    def get_content_objects(self, content_data):
        return content_data['objects']

    def get_list_api(self):
        response = self.c.get(self.entry_list_uri)
        self.assertEqual(response.status_code, 200)

        content_data = json.loads(response.content)
        objects = self.get_content_objects(content_data)
        self.assertTrue(objects)
        self.assertTrue(all([field in objects[0] for field in self.entry1_args]))

    def get_detail_api(self):
        response = self.c.get(self.entry_detail_uri)

        self.assertEqual(response.status_code, 200)
        content_data = json.loads(response.content)
        self.assertTrue(all([field in content_data for field in self.entry1_args]))

    def post_api(self, user_uri=True):
        user_key = self.user_detail_uri if user_uri else self.user1.id
        entry_copy = {'user': user_key, 'title': 'second name', 'content': 'some entry'}
        response = self.c.post(self.entry_list_uri, data=json.dumps(entry_copy),
                               content_type=JSON_TYPE)

        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(Entry.objects.count(), 2)

        entry_copy = {'user': user_key, 'title': '', 'content': 'some entry'}
        response = self.c.post(self.entry_list_uri, data=json.dumps(entry_copy),
                               content_type=JSON_TYPE)

        self.assertEqual(response.status_code, 400, response.content)

    def put_api(self, user_uri=True):
        user_key = self.user_detail_uri if user_uri else self.user1.id
        updated_fields = {'user': user_key, 'title': 'new title', 'content': 'some entry'}
        response = self.c.put(self.entry_detail_uri, data=json.dumps(updated_fields), content_type=JSON_TYPE)

        self.assertIn(response.status_code, [200, 204], response.content)
        self.entry1.refresh_from_db()
        self.assertEqual(self.entry1.title, updated_fields['title'])

    def delete_api(self):
        response = self.c.delete(self.entry_detail_uri)

        self.assertIn(response.status_code, [200, 204], response.content)
        self.assertFalse(Entry.objects.count())
