from django.contrib.auth.models import User
from django.forms import ModelForm
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.validation import Validation
from resources.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'

class EntryValidator(Validation):
    def is_valid(self, bundle, request=None):
        bundle.data['user'] = bundle.obj.user_id
        form = EntryForm(bundle.data)
        if not form.is_valid():
            return form.errors


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ('email', 'username')


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authorization = Authorization()
        validation = EntryValidator(form_class=EntryForm)


entry_resource = EntryResource()
user_resource = UserResource()

api_urls = entry_resource.urls + user_resource.urls
