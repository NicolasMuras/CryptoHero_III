from django.urls import path
from apps.songs.api.views.general_views import (
    ArtistListCreateAPIView, ArtistDetailAPIView, ArtistDestroyAPIView, ArtistUpdateAPIView,
    AlbumListCreateAPIView, AlbumDetailAPIview, AlbumDestroyAPIView, AlbumUpdateAPIView
    )
from apps.songs.api.views.song_views import (
    SongListCreateAPIView, SongRetrieveAPIView, SongDestroyAPIView, SongUpdateAPIView
    )


urlpatterns = [
    path('artistas/', ArtistListCreateAPIView.as_view(), name = 'artistas'),
    path('artistas/retrieve/<int:pk>', ArtistDetailAPIView.as_view(), name='artist_retrieve'),
    path('artistas/destroy/<int:pk>', ArtistDestroyAPIView.as_view(), name='artist_destroy'),
    path('artistas/update/<int:pk>', ArtistUpdateAPIView.as_view(), name='artist_update'),
    
    path('albumes/', AlbumListCreateAPIView.as_view(), name = 'albumes'),
    path('albumes/retrieve/<int:pk>', AlbumDetailAPIview.as_view(), name='album_retrieve'),
    path('albumes/destroy/<int:pk>', AlbumDestroyAPIView.as_view(), name='album_destroy'),
    path('albumes/update/<int:pk>', AlbumUpdateAPIView.as_view(), name='album_update'),

    path('canciones/', SongListCreateAPIView.as_view(), name = 'canciones'),
    path('canciones/retrieve/<int:pk>/', SongRetrieveAPIView.as_view(), name = 'song_retrieve'),
    path('canciones/destroy/<int:pk>/', SongDestroyAPIView.as_view(), name = 'song_destroy'),
    path('canciones/update/<int:pk>/', SongUpdateAPIView.as_view(), name = 'song_update'),
]