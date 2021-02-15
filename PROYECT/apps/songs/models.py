from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class Artist(BaseModel):

    # TODO: Define fields here:
    name = models.CharField('Nombre', max_length=100, unique = False, blank = False, null = False)
    last_name = models.CharField('Apellido', max_length=100, unique = False, blank = False, null = False)
    artist_name = models.CharField('Nombre Artistico', max_length=100, unique = True, blank = False, null = False)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
    def __unicode__(self):
        return self.artist_name

    def __str__(self):
        return self.artist_name

class Album(BaseModel):

    # TODO: Define fields here:
    name = models.CharField('Nombre', max_length=100, unique = False, null = True, blank = True)
    release_date = models.DateField()
    genre = models.CharField('Genero', max_length=50, unique = False, null = True, blank = True)
    image = models.ImageField('Tapa', upload_to='artistas/', blank = True, null = True)
    belongs_to_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name = 'Autor', null = True)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Album'
        verbose_name_plural = 'Albumes'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Song(BaseModel):

    # TODO: Define fields here:
    track_id = models.SmallIntegerField()
    name = models.CharField('Nombre', max_length=100, unique = False, null = False, blank = False)
    minutes = models.SmallIntegerField()
    seconds = models.SmallIntegerField()
    belongs_to_album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name = 'Album', null = True, blank = True)
    autor = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name = 'Autor', null = False)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Cancion'
        verbose_name_plural = 'Canciones'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name