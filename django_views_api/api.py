import json
from django.conf.urls import url
from django.core.serializers.python import Serializer
from django.forms.models import ModelForm
from django.http.response import JsonResponse
from django.utils.encoding import force_text
from django.views.generic import View
from resources.models import Entry


class CustomSerializer(Serializer):
    def get_dump_object(self, obj):
        if not self.use_natural_primary_keys or not hasattr(obj, 'natural_key'):
            self._current['id'] = force_text(obj._get_pk_val(), strings_only=True)
        return self._current


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class ApiDetailView(View):
    model = None
    form = None

    def get(self, request, *args, **kwargs):
        obj = self.model.objects.get(pk=kwargs['pk'])
        serialized_data = CustomSerializer().serialize([obj])
        return JsonResponse(data=serialized_data[0], safe=False)

    def delete(self, request, *args, **kwargs):
        self.model.objects.get(pk=kwargs['pk']).delete()
        return JsonResponse(data='', safe=False, status=204)

    def put(self, request, *args, **kwargs):
        obj = self.model.objects.get(pk=kwargs['pk'])
        data = json.loads(request.body)
        form = self.form(data=data, instance=obj)
        if form.is_valid():
            form.save()
            serialized_data = CustomSerializer().serialize([obj])
            return JsonResponse(data=serialized_data[0], status=204)
        else:
            return JsonResponse(data=form.errors, status=400)


class ApiListView(View):
    model = None
    form = None

    def get(self, request, *args, **kwargs):
        serialized_data = CustomSerializer().serialize(self.model.objects.all())
        return JsonResponse(data=serialized_data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        form = self.form(data=data)
        if form.is_valid():
            obj = form.save()
            serialized_data = CustomSerializer().serialize([obj])
            return JsonResponse(data=serialized_data[0], status=201)
        else:
            return JsonResponse(data=form.errors, status=400)


class EntryListApiView(ApiListView):
    model = Entry
    form = EntryForm


class EntryDetailApiView(ApiDetailView):
    model = Entry
    form = EntryForm


api_urls = [
    url(r'entry/$', EntryListApiView.as_view(), name='entry-list-django-view'),
    url(r'entry/(?P<pk>\d+)/$', EntryDetailApiView.as_view(), name='entry-detail-django-view'),
]
