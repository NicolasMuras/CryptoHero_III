from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

SONGS_URL_PATH = 'apps.songs.api.urls'
PAYMENTS_URL_PATH = 'apps.payments.api.urls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(SONGS_URL_PATH)),
    path('api/', include(PAYMENTS_URL_PATH)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
