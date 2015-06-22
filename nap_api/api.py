import json

from django.contrib.auth.models import User
from django.forms import ModelForm
from nap import serialiser, rest
from nap.rest.views import ObjectDeleteMixin

from resources.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class EntrySerialiser(serialiser.ModelSerialiser):
    def object_inflate(self, data, instance=None, **kwargs):
        form = EntryForm(data)
        if not form.is_valid():
            raise ValueError(form.errors)
        obj = super(EntrySerialiser, self).object_inflate(data, instance, **kwargs)
        return obj

    def deflate_user(self, obj, data, **kwargs):
        return obj.user_id

    def inflate_user(self, data, obj, instance, **kwargs):
        return User.objects.get(pk=data['user'])

    class Meta:
        model = Entry


class EntryPublisher(ObjectDeleteMixin, rest.ModelPublisher):
    api_name = 'entry'
    serialiser = EntrySerialiser()

    def object_delete_default(self, request, object_id, **kwargs):
        self.serialiser._meta.model.objects.get(pk=object_id).delete()
        return self.create_response('')

    def object_put_default(self, request, object_id, **kwargs):
        data = json.loads(request.body)
        obj = self.serialiser.object_inflate(data, Entry.objects.get(pk=object_id))
        obj.save()
        return self.render_single_object(obj)


rest.api.register('api', EntryPublisher)
rest.api.autodiscover()
api_urls = rest.api.patterns()
