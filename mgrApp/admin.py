from django.contrib import admin
from .models import Client, Musician
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'artist_name']


class MusicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'band', 'instrument']


admin.site.register(Client, ClientAdmin)
admin.site.register(Musician, MusicianAdmin)
