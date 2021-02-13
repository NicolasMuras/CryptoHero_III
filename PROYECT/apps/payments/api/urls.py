from django.urls import path
from apps.payments.api.views.general_views import LocationListAPIView
from apps.payments.api.views.payment_views import PayListAPIView

urlpatterns = [
    path('pagos/', PayListAPIView.as_view(), name = 'pagos'),
    path('locations/', LocationListAPIView.as_view(), name = 'locations'),
]