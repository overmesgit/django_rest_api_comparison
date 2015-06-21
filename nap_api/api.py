from nap import serialiser, rest
from resources.models import Entry


class EntrySerialiser(serialiser.ModelSerialiser):
    def deflate_user(self, obj, data, **kwargs):
        return obj.user_id

    class Meta:
        model = Entry


class EntryPublisher(rest.ModelPublisher):
    api_name = 'entry'

    serialiser = EntrySerialiser()


rest.api.register('', EntryPublisher)
rest.api.autodiscover()
api_urls = rest.api.patterns()
