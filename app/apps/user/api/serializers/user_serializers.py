from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        modele = get_user_model()
        fields = ('email', 'password', 'artist_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        # Crear usuario con contraseña encriptada y devolverlo.
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style = {'input_type': 'password'}, trim_whitespace = False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Credenciales incorrectas.')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs