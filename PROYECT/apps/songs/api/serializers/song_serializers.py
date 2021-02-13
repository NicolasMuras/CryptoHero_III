from rest_framework import serializers
from apps.songs.models import Song
from apps.songs.api.serializers.general_serializers import ArtistSerializer, AlbumSerializer

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        if instance.seconds < 9:
            duration = str(instance.minutes) + ':0' + str(instance.seconds)
        else:
            duration = str(instance.minutes) + ':' + str(instance.seconds)

        return {
            'Track': instance.track_id,
            'Nombre': instance.name,
            'Album': instance.belongs_to_album.name,
            'Artista': instance.belongs_to_album.belongs_to_artist.artist_name,
            'Duración': duration
        }
