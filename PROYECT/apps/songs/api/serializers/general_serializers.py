from apps.songs.models import Album, Artist
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'ID': instance.id,
            'Titulo': instance.name,
            'Fecha de lanzamiento': instance.release_date,
            'Tapa': instance.image if instance.image != '' else '',
            'Artista': instance.belongs_to_artist.artist_name,
        }

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'ID': instance.id,
            'Nombre': instance.name,
            'Apellido': instance.last_name,
            'Nombre artistico': instance.artist_name,
        }