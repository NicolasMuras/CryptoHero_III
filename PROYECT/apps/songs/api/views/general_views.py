
from apps.base.api import GeneralListAPIView
from apps.songs.api.serializers.general_serializers import AlbumSerializer, ArtistSerializer

class AlbumListAPIView(GeneralListAPIView):
    serializer_class = AlbumSerializer

class ArtistListAPIView(GeneralListAPIView):
    serializer_class = ArtistSerializer