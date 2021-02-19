from rest_framework import serializers
from apps.songs.models import Song
from apps.songs.api.serializers.general_serializers import ListArtistSerializer, ListAlbumSerializer


#############################################[  GLOBALS  ]############################################

BLANK_SPACE = 'Espacio vacio.'
INVALID_RANGE = 'El numero esta fuera del rango permitido.'

def comprobar_rango_tiempo(value):
        # custom validation: los minutos deben tener un rango de valores que se refleje a la realidad.
        if value > 60 or value < 0:
            raise serializers.ValidationError(INVALID_RANGE)

def comprobar_espacio_vacio(value):
        # custom validation: comprobamos que el valor no este en blanco.
        if value == '':
            raise serializers.ValidationError(BLANK_SPACE)

def serializa_si_existe(instance):
    # Serializa solamente si el objeto existe, en caso contrario, devuelve una cadena vacia.
    try:
        if instance.belongs_to_album.name != '':
            return instance.belongs_to_album.name
                
    except Exception:
        return ''

######################################################################################################

class ListSongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        # Excluimos attributos que no seran consumidos por el frontend, pero sirven en backend, aplicamos el principio de encapsulación.
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    # Nos permite representar de una forma diferente los datos.
    def to_representation(self, instance):
        # Validacion custom: En caso el numero de segundos sea de una cifra se agrega un 0 a la izquierda.
        if instance.seconds < 9:
            duration = str(instance.minutes) + ':0' + str(instance.seconds)
        else:
            duration = str(instance.minutes) + ':' + str(instance.seconds)

        return {
            'id': instance.id,
            'Track': instance.track_id,
            'Nombre': instance.name,
            'Album': serializa_si_existe(instance),
            'Artista': instance.autor.artist_name,
            'Duración': duration
        }


class DetailSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class CreateUpdateSongSerializer(serializers.ModelSerializer):
    
    track_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    minutes = serializers.IntegerField()
    seconds = serializers.IntegerField()
    belongs_to_album = ListAlbumSerializer.Meta.model.objects.all().values('name')
    autor = ListArtistSerializer.Meta.model.objects.all().values('artist_name')

    class Meta:
        model = Song
        fields = ('track_id', 'name', 'minutes', 'seconds', 'belongs_to_album', 'autor',)

    def validate_track_id(self, value):
        comprobar_espacio_vacio(value)
        return value

    def validate_name(self, value):
        comprobar_espacio_vacio(value)
        return value

    def validate_minutes(self, value):
        comprobar_rango_tiempo(value)
        return value

    def validate_seconds(self, value):
        comprobar_rango_tiempo(value)
        return value

    def validate_belongs_to_album(self, value):

        return value

    def validate_autor(self, value):

        return value

    def validate(self, data):
        return data


class CreateSongSerializer(CreateUpdateSongSerializer):

    def create(self, validated_data):
        song = Song(**validated_data)
        song.save()
        return song


class UpdateSongSerializer(CreateUpdateSongSerializer):

    def update(self, instance, validated_data):
        instance.track_id = validated_data.get('track_id', instance.track_id)
        instance.name = validated_data.get('name', instance.name)
        instance.minutes = validated_data.get('minutes', instance.minutes)
        instance.seconds = validated_data.get('seconds', instance.seconds)
        instance.belongs_to_album = validated_data.get('belongs_to_album', instance.belongs_to_album)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.save()
        return instance