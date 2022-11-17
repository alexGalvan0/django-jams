from rest_framework import serializers
from .models import Song, Artist, Playlist, Album, Genre
from pprint import pprint as pp


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('__all__')


class AlbumSerializer(serializers.ModelSerializer):
   # artist = ArtistSerializer(many=True)
    class Meta:
        model = Album
        fields = ['name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)

    class Meta:
        model = Song
        fields = '__all__'
