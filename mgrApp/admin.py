from django.contrib import admin
from .models import Client, Musician
from guardian.admin import GuardedModelAdmin

# Register your models here.


class ClientAdmin(GuardedModelAdmin):
    list_display = ['id', 'artist_name']


class MusicianAdmin(GuardedModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'band', 'instrument']


admin.site.register(Client, ClientAdmin)
admin.site.register(Musician, MusicianAdmin)
