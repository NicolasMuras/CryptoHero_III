from rest_framework import generics
from apps.base.api import GeneralListAPIView
from apps.payments.api.serializers.general_serializers import LocationSerializer

class LocationListAPIView(GeneralListAPIView):
    serializer_class = LocationSerializer
