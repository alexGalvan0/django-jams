from rest_framework import serializers
from .models import Song, Artist, Playlist, Album, Genre
from pprint import pprint as pp


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('__all__')


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'name', 'image', 'year_released','songs']

    def get_songs(self,obj):
        album_id = obj.id
        pp(album_id)
        songs = Song.objects.filter(album = album_id)
        pp(songs)
        album_songs = []
        for song in songs:
            album_songs.append({"id":song.id,"name":song.name})
        return album_songs
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)

    class Meta:
        model = Song
        fields = ['id', 'name', 'album', 'artist']
