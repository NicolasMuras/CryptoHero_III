from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from apps.payments.models import Pay, Location
from apps.payments.api.serializers.payment_serializers import PaySerializer, LocationSerializer, DetailPaySerializer, DetailLocationSerializer

class LocationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        return self.queryset.filter(state = True).order_by('-id')
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            print('hello')
            return DetailLocationSerializer
        else:
            print('hola')
            return LocationSerializer

    def perform_create(self, serializer):
        serializer.save()

class PayViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer

    def get_queryset(self):
        return self.queryset.filter(state = True).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailPaySerializer
        else:
            return PaySerializer

    def perform_create(self, serializer):
        serializer.save()
