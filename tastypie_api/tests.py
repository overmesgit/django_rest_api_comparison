from django.core.urlresolvers import reverse

from resources.tests import ApiTestCase


class TastyPieTest(ApiTestCase):

    def setUp(self):
        super(TastyPieTest, self).setUp()
        self.entry_list_uri = reverse('api_dispatch_list', args=('entry',))
        self.entry_detail_uri = reverse('api_dispatch_detail', args=('entry', self.entry1.id))
        self.user_detail_uri = reverse('api_dispatch_detail', args=('user', self.user1.id))

    def get_content_objects(self, content_data):
        return content_data['objects']

    def test_get_list_api(self):
        self.get_list_api()

    def test_get_detail_api(self):
        self.get_detail_api()

    def test_post_api(self):
        self.post_api()

    def test_put_api(self):
        self.put_api()

    def test_delete_api(self):
        self.delete_api()
