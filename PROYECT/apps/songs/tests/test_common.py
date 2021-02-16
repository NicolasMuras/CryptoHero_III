from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from apps.songs.models import Song
from apps.songs.api.serializers.song_serializers import ListSongSerializer

SONG_URL = reverse('api:canciones')

class SongAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_song_list(self):
        # Devuelve un listado de canciones.
        Song.objects.create(self, name='Rainmaker')
        Song.objects.create(self, name='Shoot To Thrill')

        res = self.client.get(SONG_URL)

        songs = Song.object.all().order_by('-name')
        serializer = ListSongSerializer(songs, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


