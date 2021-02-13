from apps.songs.models import Album, Artist
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')