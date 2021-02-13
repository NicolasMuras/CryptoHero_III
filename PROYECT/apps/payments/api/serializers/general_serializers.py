from apps.payments.models import Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        # Data filter:
        exclude = ('state', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'Direccion': instance.address,
            'Ciudad': instance.city,
            'Estado': instance.state,
            'Coordenada Y':  instance.y_coord,
            'Coordenada X':  instance.x_coord,
        }