from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.songs.api.serializers.general_serializers import ListAlbumSerializer, DetailAlbumSerializer, CreateUpdateAlbumSerializer, ListArtistSerializer, DetailArtistSerializer, CreateUpdateArtistSerializer


#############################################[  Album  ]############################################

class AlbumListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ListAlbumSerializer
    queryset = DetailAlbumSerializer.Meta.model.objects.filter(state = True)

    # Sobreescribimos la función post para presentar un mensaje al crear un objeto.
    def post (self, request):
        serializer = CreateUpdateAlbumSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Álbum creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AlbumDetailAPIview(generics.RetrieveAPIView):
    serializer_class = DetailAlbumSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


class AlbumDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ListAlbumSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    # Sobre escribimos la función delete para efectuar una eliminación logica,
    # se cambia el estado del objeto a 'False' para representar esto.
    def delete(self, request, pk=None):
        song = self.get_queryset().filter(id = pk).first()
        if song:
            song.state = False
            song.save()
            return Response({'message':'Artista eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una artista con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


class AlbumUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CreateUpdateAlbumSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            object_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(object_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un álbum con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            object_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if object_serializer.is_valid():
                object_serializer.save()
                return Response(object_serializer.data, status = status.HTTP_200_OK)
            return Response(object_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#############################################[  Artist  ]############################################

class ArtistListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ListArtistSerializer
    queryset = DetailArtistSerializer.Meta.model.objects.filter(state = True)

    # Sobreescribimos la función post para presentar un mensaje al crear un objeto.
    def post (self, request):
        serializer = CreateUpdateArtistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Artista creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ArtistDetailAPIView(generics.RetrieveAPIView):
    serializer_class = DetailArtistSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


class ArtistDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ListArtistSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True) 

    # Sobre escribimos la función delete para efectuar una eliminación logica,
    # se cambia el estado del objeto a 'False' para representar esto.
    def delete(self, request, pk=None):
        object_ = self.get_queryset().filter(id = pk).first()
        if object_:
            object_.state = False
            object_.save()
            return Response({'message':'Artista eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una artista con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


class ArtistUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CreateUpdateArtistSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            object_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(object_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un artista con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            object_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if object_serializer.is_valid():
                object_serializer.save()
                return Response(object_serializer.data, status = status.HTTP_200_OK)
            return Response(object_serializer.errors, status = status.HTTP_400_BAD_REQUEST)