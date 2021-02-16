from django.urls import path
from apps.songs.api.views.general_views import ArtistListAPIView, AlbumListAPIView
from apps.songs.api.views.song_views import (
    SongListCreateAPIView, SongDestroyAPIView, SongRetrieveAPIView, SongUpdateAPIView
    )

urlpatterns = [
    path('artistas/', ArtistListAPIView.as_view(), name = 'artistas'),
    path('albumes/', AlbumListAPIView.as_view(), name = 'albumes'),
    path('canciones/', SongListCreateAPIView.as_view(), name = 'canciones'),
    path('canciones/retrieve/<int:pk>/', SongRetrieveAPIView.as_view(), name = 'song_retrieve'),
    path('canciones/destroy/<int:pk>/', SongDestroyAPIView.as_view(), name = 'song_destroy'),
    path('canciones/update/<int:pk>/', SongUpdateAPIView.as_view(), name = 'song_update'),
]