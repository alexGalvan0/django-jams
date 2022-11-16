from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer
from .models import Song, Album, Artist, Genre, Playlist
from rest_framework import permissions
from rest_framework import viewsets
# Create your views here.

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]

    