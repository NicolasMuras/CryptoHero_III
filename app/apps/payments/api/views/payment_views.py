from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.payments.models import Pay, Location
from apps.payments.api.serializers.payment_serializers import PaySerializer, LocationSerializer, DetailPaySerializer, DetailLocationSerializer


class LocationViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
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
        # Devuelve objetos solamente para el usuario autenticado.
        return self.queryset.filter(user=self.request.user).order_by('-address')
        #return self.queryset.filter(state = True).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PayViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
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
        return self.queryset.filter(user=self.request.user).order_by('-quantity')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)