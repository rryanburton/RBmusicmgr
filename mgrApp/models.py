import os

from django.db import models

# Create your models here.
class Client(models.Model):
    artist_name = models.CharField(max_length=20)


    class Meta:
            verbose_name = 'Client'
            verbose_name_plural = 'Clients'
            ordering = ['artist_name']

    def __str__(self):
        return ("{}".format(self.artist_name))


class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    ss_num = models.CharField(max_length=20, blank=True, null=True)
    drivers_license = models.ImageField(upload_to='static/img/', blank=True, null=True)
    passport = models.ImageField(upload_to='static/img/', blank=True, null=True)
    form_w9 = models.ImageField(upload_to='static/img/', blank=True, null=True)
    instrument = models.CharField(max_length=20, blank=True, null=True)
    band = models.ForeignKey(Client)

    class Meta:
            verbose_name = 'Musician'
            verbose_name_plural = 'Musicians'
            ordering = ['band', 'last_name']

    def __str__(self):
        return ("{} {} from {}".format(self.first_name, self.last_name, self.band))


class AudioFiles(models.Model):
    band = models.ForeignKey(Client)
    display_name = models.CharField(max_length=20)
    file_name =
    type =
    audio_file =


class ImageFiles(models.Model):
    band = models.ForeignKey(Client)
    display_name = models.CharField(max_length=20)
    file_name =
    type =
    image_file =