from rest_framework import serializers
from apps.payments.models import Pay, Location


#############################################[  Location  ]############################################

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ('state', 'modified_date', 'deleted_date')
        read_only_fields = ('id',)

    def to_representation(self, instance):

        return {
            'ID': instance.id,
            'Direccion': instance.address,
            'Ciudad': instance.city,
            'Estado': instance.state_name,
            'Coordenada X':  instance.x_coord,
            'Coordenada Y':  instance.y_coord,
        }

    def validate(self, data):
        return data


class DetailLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

#############################################[  Pay  ]#################################################

class PaySerializer(serializers.ModelSerializer):
    
    location = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Location.objects.all()
    )
    
    class Meta:
        model = Pay
        fields = ('id', 'quantity', 'cryptocurrency', 'wallet_address', 'location')
        read_only_fields = ('id',)

    def validate(self, data):
        return data


class DetailPaySerializer(PaySerializer):

    location = LocationSerializer(many=False, read_only=True)
