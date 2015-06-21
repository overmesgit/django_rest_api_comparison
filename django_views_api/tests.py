from django.core.urlresolvers import reverse

from resources.tests import ApiTestCase


class DjangoViewApiTest(ApiTestCase):

    def setUp(self):
        super(DjangoViewApiTest, self).setUp()
        self.entry_list_uri = reverse('entry-list-django-view')
        self.entry_detail_uri = reverse('entry-detail-django-view', args=(self.entry1.id, ))

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
