from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer
from .models import Song, Album, Artist, Genre, Playlist
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from pprint import pprint as pp


# Create your views here.

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    # returns songs from artist

    @action(detail=True, methods=['GET'])
    def getSongsByArtist(self, request, **kwargs):
        id = self.kwargs.get('pk')
        songs = Song.objects.filter(artist__id=id)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

# add song to artist


@api_view(['POST', 'DELETE'])
def addArtistToSong(request, artistId, songId):
    if request.method == 'POST':
        song = Song.objects.get(id=songId)
        artist = Artist.objects.get(id=artistId)
        song.artist.add(artist)
        song.save()
        songSerializer = SongSerializer(song)
        return Response(songSerializer.data)

    if request.method == 'DELETE':
        song = Song.objects.get(id=songId)
        artist = Artist.objects.get(id=artistId)
        song.artist.remove(artist)
        song.save()
        songSerializer = SongSerializer(song)
        return Response(songSerializer.data)

# add song to album


@api_view(['POST', 'DELETE'])
def addSongToAlbum(request, albumId, songId):
    song = Song.objects.get(id=songId)
    album = Album.objects.get(id=albumId)

    if request.method == 'POST':
        song.album.add(album)
        song.save()
        songSerializer = SongSerializer(song)
        return Response(songSerializer.data)
    if request.method == 'DELETE':
        song.album.remove(album)
        song.save()
        songSerializer = SongSerializer(song)
        return Response(songSerializer.data)




class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # want to get evreysong from genre
    @action(detail=True, methods=['GET'])
    def getSongsByGenre(self, request, **kwargs):
        id = self.kwargs.get('pk')
        songs = Song.objects.filter(genre__id=id)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# want to get all songs from playlist
    @action(detail=True, methods=['GET'])
    def getSongsByPlaylist(self, request, **kwargs):
        id = self.kwargs.get('pk')
        songs = Song.objects.filter(playlist__id=id)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

#  want to return all songs from album
    @action(detail=True, methods=['GET'])
    def getSongByAlbum(self, request, **kwargs):

        id = self.kwargs.get('pk')
        songs = Song.objects.filter(album__id=id)
        serilazier = SongSerializer(songs, many=True)

        return Response(serilazier.data)
