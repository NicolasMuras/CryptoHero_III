from rest_framework import serializers
from apps.payments.models import Pay, Location


#############################################[  Location  ]############################################

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ('state', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'Direccion': instance.address,
            'Ciudad': instance.city,
            'Estado': instance.state_name,
            'Coordenada X':  instance.x_coord,
            'Coordenada Y':  instance.y_coord,
        }

    def validate(self, data):
        print(data)
        return data


class DetailLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

#############################################[  Pay  ]#################################################

class PaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pay
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'Cantidad': instance.quantity,
            'Criptodivisa': instance.cryptocurrency,
            'Coordenada X': instance.location.x_coord,
            'Coordenada Y': instance.location.y_coord,
            'Wallet': instance.wallet_address,
        }
    def validate(self, data):
        return data


class DetailPaySerializer(PaySerializer):

    location = LocationSerializer(many=True, read_only=True)
