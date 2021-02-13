from django.contrib import admin
from django.urls import path, include

SONGS_URL_PATH = 'apps.songs.api.urls'
PAYMENTS_URL_PATH = 'apps.payments.api.urls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artistas/', include(SONGS_URL_PATH)),
    path('albumes/', include(SONGS_URL_PATH)),
    path('canciones/', include(SONGS_URL_PATH)),
    path('pagos/', include(PAYMENTS_URL_PATH)),
    path('locations', include(PAYMENTS_URL_PATH)),
]
