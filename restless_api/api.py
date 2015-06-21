from django.conf.urls import url
from restless.modelviews import ListEndpoint, DetailEndpoint
from resources.models import Entry


class MyList(ListEndpoint):
    model = Entry


class MyDetail(DetailEndpoint):
    model = Entry


api_urls = [
    url(r'entry/$', MyList.as_view(), name='entry-list-restless'),
    url(r'entry/(?P<pk>\d+)/$', MyDetail.as_view(), name='entry-detail-restless'),
]
