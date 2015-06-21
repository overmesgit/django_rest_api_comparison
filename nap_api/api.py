from django.contrib.auth.models import User
from django.forms import ModelForm
from nap import serialiser, rest
from resources.models import Entry
from django.core.exceptions import ValidationError


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class EntrySerialiser(serialiser.ModelSerialiser):
    def object_inflate(self, data, instance=None, **kwargs):
        data = super(EntrySerialiser, self).object_inflate(data, instance, **kwargs)
        form = EntryForm(instance=data)
        if not form.is_valid():
            raise ValidationError(form.errors)
        return data

    def deflate_user(self, obj, data, **kwargs):
        return obj.user_id

    def inflate_user(self, data, obj, instance, **kwargs):
        return User.objects.get(pk=data['user'])

    class Meta:
        model = Entry


class EntryPublisher(rest.ModelPublisher):
    api_name = 'entry'
    serialiser = EntrySerialiser()


rest.api.register('api', EntryPublisher)
rest.api.autodiscover()
api_urls = rest.api.patterns()
