from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer
from .models import Song, Album, Artist, Genre, Playlist
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from pprint import pprint as pp


# Create your views here.

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


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
