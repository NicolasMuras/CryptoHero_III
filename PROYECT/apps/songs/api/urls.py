from django.urls import path
from apps.songs.api.views.general_views import ArtistListAPIView, AlbumListAPIView
from apps.songs.api.views.song_views import SongListAPIView

urlpatterns = [
    path('artistas/', ArtistListAPIView.as_view(), name = 'artistas'),
    path('albumes/', AlbumListAPIView.as_view(), name = 'albumes'),
    path('canciones/', SongListAPIView.as_view(), name = 'canciones'),
]