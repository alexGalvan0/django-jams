from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer
from .models import Song, Album, Artist, Genre, Playlist
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pprint import pprint as pp


# Create your views here.

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


    #returns songs from artist
    @action(detail=True, methods=['GET'])
    def getSongsByArtist(self, request, **kwargs):
        id = self.kwargs.get('pk')
        songs = Song.objects.filter(artist__id=id)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

#add song to artist
@api_view(['GET'])
def addArtistToSong(request,artistId,songId):
    song = Song.objects.get(id=songId)
    artist = Artist.objects.get(id=artistId)
    song.artist.add(artist)
    song.save()
    songSerializer = SongSerializer(song)
    artistSerializer = ArtistSerializer(artist)

    return Response(artistSerializer.data)    
        
        



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
