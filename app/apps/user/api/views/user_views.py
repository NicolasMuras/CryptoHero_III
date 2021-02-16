from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from apps.user.api.serializers.user_serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    # Crea un nuevo usuario en el sistema.
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    # Crea un nuevo token para el usuario.
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES