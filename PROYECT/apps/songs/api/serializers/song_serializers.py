from rest_framework import serializers
from apps.songs.models import Song
from apps.songs.api.serializers.general_serializers import ArtistSerializer, AlbumSerializer

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        
        duration = str(instance.minutes) + ':' + str(instance.seconds)

        return {
            'id': instance.id,
            'name': instance.name,
            'album': instance.belongs_to_album.name,
            'artist': instance.belongs_to_album.belongs_to_artist.name,
            'duration': duration
        }
