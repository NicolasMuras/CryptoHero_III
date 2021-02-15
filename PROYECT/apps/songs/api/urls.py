from django.urls import path
from apps.songs.api.views.general_views import ArtistListAPIView, AlbumListAPIView
from apps.songs.api.views.song_views import (
    SongListAPIView, SongCreateAPIView, SongDestroyAPIView, SongRetrieveAPIView, SongUpdateAPIView
    )

urlpatterns = [
    path('artistas/', ArtistListAPIView.as_view(), name = 'artistas'),
    path('albumes/', AlbumListAPIView.as_view(), name = 'albumes'),
    path('canciones/list/', SongListAPIView.as_view(), name = 'song_list'),
    path('canciones/create/', SongCreateAPIView.as_view(), name = 'song_create'),
    path('canciones/retrieve/<int:pk>/', SongRetrieveAPIView.as_view(), name = 'song_retrieve'),
    path('canciones/destroy/<int:pk>/', SongDestroyAPIView.as_view(), name = 'song_destroy'),
    path('canciones/update/<int:pk>/', SongUpdateAPIView.as_view(), name = 'song_update'),
]