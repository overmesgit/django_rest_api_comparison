from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_api.api import router
from tastypie_api.api import api_urls as tastypie_api_urls
from django_views_api.api import api_urls as django_api_urls
from restless_api.api import api_urls as restless_api_urls
from nap_api.api import api_urls as nap_api_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^tastypie/', include(tastypie_api_urls)),
    url(r'^rest_framework/', include(router.urls)),
    url(r'^django_view/', include(django_api_urls)),
    url(r'^restless/', include(restless_api_urls)),
    url(r'^nap/', include(nap_api_urls)),
]
