from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

# default  viewsets
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'playlists', views.PlaylistViewSet)


# quer viewsets

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('addArtistToSong/<int:artistId>/<int:songId>/', views.addArtistToSong),
    path('addSongToAlbum/<int:albumId>/<int:songId>', views.addSongToAlbum),
    path('addSongToPlaylist/<int:playlistID>/<int:songID>', views.addSongToPlaylist),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
