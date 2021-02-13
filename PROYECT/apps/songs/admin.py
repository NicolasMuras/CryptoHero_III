from django.contrib import admin
from apps.songs.models import *

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)