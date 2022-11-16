from rest_framework import serializers
from .models import Song,Artist,Playlist,Album,Genre

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('__all__')
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('__all__')
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