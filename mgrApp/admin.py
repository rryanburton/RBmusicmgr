from django.contrib import admin
from .models import Client, Musician, AudioFiles, ImageFiles, Manager
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'artist_name']


class MusicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'band', 'instrument']

class AudioFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'band', 'display_name']

class ImageFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'band', 'display_name']

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

admin.site.register(Client, ClientAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(AudioFiles, AudioFilesAdmin)
admin.site.register(ImageFiles, ImageFilesAdmin)
admin.site.register(Manager, ManagerAdmin)
