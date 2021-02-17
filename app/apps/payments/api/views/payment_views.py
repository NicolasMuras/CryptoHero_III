from rest_framework import viewsets, mixins
from apps.payments.models import Pay, Location
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.payments.api.serializers.payment_serializers import PaySerializer, LocationSerializer, DetailPaySerializer, DetailLocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = DetailLocationSerializer(location)
        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.filter(state = True).order_by('-id')

class PayViewSet(viewsets.ModelViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer

    def list(self, request):
        queryset = Pay.objects.all()
        serializer = PaySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Pay.objects.all()
        pay = get_object_or_404(queryset, pk=pk)
        serializer = DetailPaySerializer(pay)
        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.filter(state = True).order_by('-id')
