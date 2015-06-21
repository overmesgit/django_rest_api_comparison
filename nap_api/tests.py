from django.core.urlresolvers import reverse

from resources.tests import ApiTestCase


class NapApiTest(ApiTestCase):

    def setUp(self):
        super(NapApiTest, self).setUp()
        self.entry_list_uri = reverse('entry_list_default')
        self.entry_detail_uri = reverse('entry_object_default', args=(self.entry1.id, ))

    def get_content_objects(self, content_data):
        return content_data['objects']

    def test_get_list_api(self):
        self.get_list_api()

    def test_get_detail_api(self):
        self.get_detail_api()

    def test_post_api(self):
        self.post_api(user_uri=False)

    def test_put_api(self):
        self.put_api(user_uri=False)

    def test_delete_api(self):
        self.delete_api()
