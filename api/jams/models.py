from django.db import models


# Create your models here.


class Song(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    genre = models.ForeignKey(
        'Genre', on_delete=models.PROTECT, blank=False, null=False)
    artist = models.ManyToManyField('Artist', blank=False)
    played = models.BigIntegerField(default=0)
    liked = models.BooleanField(default=None)
    album = models.ManyToManyField('Album')
    playlist = models.ManyToManyField('Playlist')
    lyrics = models.TextField(max_length=5000, default='')
    duration = models.TimeField(null=True, blank=True, default=None)


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.URLField(max_length=255, default='', blank=True, null=True)


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)
    bio = models.TextField(max_length=1000)
    image = models.URLField(max_length=255, default='', blank=True, null=True)


class Playlist(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.URLField(max_length=255, default='', blank=True, null=True)
    description = models.TextField(max_length=1000)


class Album(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.URLField(max_length=255, default='', blank=True, null=True)
    artist = models.ManyToManyField(Artist)
