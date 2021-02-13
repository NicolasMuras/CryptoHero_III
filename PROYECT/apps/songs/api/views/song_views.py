from apps.base.api import GeneralListAPIView
from apps.songs.api.serializers.song_serializers import SongSerializer

class SongListAPIView(GeneralListAPIView):
    serializer_class = SongSerializer