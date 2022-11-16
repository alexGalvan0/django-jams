from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

#current year
today = datetime.datetime.now()
currentYear = today.year


# Create your models here.

class Song(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    genre = models.ForeignKey(
        'Genre', on_delete=models.PROTECT, blank=False, null=False)
    artist = models.ManyToManyField('Artist', blank=False)
    played = models.BigIntegerField(default=0)
    liked = models.BooleanField(default=None)
    album = models.ManyToManyField('Album')
    playlist = models.ManyToManyField('Playlist', default=None, blank=True)
    lyrics = models.TextField(max_length=5000, default='')
    duration = models.TimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.URLField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)
    bio = models.TextField(max_length=1000)
    image = models.URLField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.URLField(max_length=255, default='', blank=True, null=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.URLField(max_length=255, default='', blank=True, null=True)
    artist = models.ManyToManyField(Artist)
    year_released = models.PositiveIntegerField(
        validators=[MinValueValidator(1700), MaxValueValidator(currentYear)], default=None)

    def __str__(self):
        return self.name
