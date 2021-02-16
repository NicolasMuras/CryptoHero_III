from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.payments.api.views import payment_views

router = DefaultRouter()
router.register('locations', payment_views.LocationViewSet)
router.register('payments', payment_views.PayViewSet)

app_name = 'payment'

urlpatterns = [
    path('', include(router.urls))
]