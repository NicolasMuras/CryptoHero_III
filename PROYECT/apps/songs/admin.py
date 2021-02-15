from django.contrib import admin
from apps.songs.models import *

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist_name')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)