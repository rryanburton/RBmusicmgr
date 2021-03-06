"""RBmusicmgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view

from mgrApp.models import Client, Musician, Manager, AudioFiles, ImageFiles


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class AudioFilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AudioFiles
        fields = '__all__'


class ImageFilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageFiles
        fields = '__all__'


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class AudioFilesViewSet(viewsets.ModelViewSet):
    queryset = AudioFiles.objects.all()
    serializer_class = AudioFilesSerializer


class ImageFilesViewSet(viewsets.ModelViewSet):
    queryset = ImageFiles.objects.all()
    serializer_class = ImageFilesSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'musicians', MusicianViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'audio-files', AudioFilesViewSet)
router.register(r'images', ImageFilesViewSet)

swagger_view = get_swagger_view()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls,),
    url(r'^docs/', swagger_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
