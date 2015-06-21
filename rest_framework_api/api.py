from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import routers
from rest_framework import serializers
from resources.models import Entry


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet)
router.register(r'user', UserViewSet)
