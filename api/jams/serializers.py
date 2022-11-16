from rest_framework import serializers
from .models import Song, Artist, Playlist, Album, Genre
from pprint import pprint as pp


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('__all__')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('__all__')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        album = validated_data.pop('album')
        instance = Album.objects.get(id = album['id'])
        song = Song.objects.create(**validated_data, album = instance)
        pp(validated_data)