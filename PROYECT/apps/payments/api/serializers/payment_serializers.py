from rest_framework import serializers
from apps.payments.models import Pay
from apps.payments.api.serializers.general_serializers import LocationSerializer

class PaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pay
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'Cantidad': instance.quantity,
            'Criptodivisa': instance.cryptocurrency,
            'Coordenadas': "X: " + instance.location.x_coord + " Y:" + instance.location.y_coord,
            'Wallet': instance.wallet_address,
        }
