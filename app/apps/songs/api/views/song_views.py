from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.songs.api.serializers.song_serializers import DetailSongSerializer, ListSongSerializer, CreateUpdateSongSerializer

#############################################[  Song  ]############################################

class SongListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ListSongSerializer
    queryset = DetailSongSerializer.Meta.model.objects.filter(state = True)

    # Sobreescribimos la función post para presentar un mensaje al crear un objeto.
    def post (self, request):
        serializer = CreateUpdateSongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Canción creada correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class SongRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DetailSongSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

class SongDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ListSongSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    # Sobre escribimos la función delete para efectuar una eliminación logica,
    # se cambia el estado del objeto a 'False' para representar esto.
    def delete(self, request, pk=None):
        song = self.get_queryset().filter(id = pk).first()
        if song:
            song.state = False
            song.save()
            return Response({'message':'Canción eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una canción con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

class SongUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CreateUpdateSongSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            song_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(song_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una canción con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            song_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if song_serializer.is_valid():
                song_serializer.save()
                return Response(song_serializer.data, status = status.HTTP_200_OK)
            return Response(song_serializer.errors, status = status.HTTP_400_BAD_REQUEST)