from django.contrib import admin
from apps.payments.models import Pay, Location
from apps.songs.models import Artist, Album, Song
from apps.user.models import User

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist_name')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)

admin.site.register(Location)
admin.site.register(Pay)
admin.site.register(User)