from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    artist_name = models.CharField(max_length=20)


    class Meta:
            verbose_name = 'Client'
            verbose_name_plural = 'Clients'
            ordering = ['artist_name']
            permissions = (
                ('view_client', 'View client'),
            )
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
    file_name = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    audio_file = models.FileField(upload_to='uploads/')

    class Meta:
            verbose_name = 'Audio File'
            verbose_name_plural = 'Audio Files'
            ordering = ['band', 'display_name', 'type']

    def __str__(self):
        return ("{} - {} - {}".format(self.band, self.display_name, self.type))

class ImageFiles(models.Model):
    band = models.ForeignKey(Client)
    display_name = models.CharField(max_length=20)
    file_name = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    image_file = models.FileField(upload_to='uploads/')

    class Meta:
            verbose_name = 'Image File'
            verbose_name_plural = 'Image Files'
            ordering = ['band', 'display_name', 'type']

    def __str__(self):
        return ("{} - {} - {}".format(self.band, self.display_name, self.type))


class Manager(models.Model):
    user = models.ForeignKey(User)
    bands = models.ManyToManyField(Client)

    class Meta:
            verbose_name = 'Manager'
            verbose_name_plural = 'Managers'


    def __str__(self):
        return ("{} - {} ".format(self.user, self.bands))