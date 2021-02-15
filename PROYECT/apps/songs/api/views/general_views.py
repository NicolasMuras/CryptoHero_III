
from apps.base.api import GeneralListAPIView
from apps.songs.api.serializers.general_serializers import ListAlbumSerializer, ListArtistSerializer

class AlbumListAPIView(GeneralListAPIView):
    serializer_class = ListAlbumSerializer

class ArtistListAPIView(GeneralListAPIView):
    serializer_class = ListArtistSerializer