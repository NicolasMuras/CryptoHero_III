from apps.songs.models import Album, Artist
from rest_framework import serializers
from datetime import datetime


#############################################[  GLOBALS  ]############################################

BLANK_SPACE = 'Espacio vacio.'
GENRES = ['Rock', 'Jazz', 'Blues', 'Heavy Metal', 'Pop', 'Classic', 'Synthwave']
INCORRECT_DATE = 'Fecha incorrecta.'
INVALID_GROUP = 'El objeto no entra en esta categoria.'

def comprobar_fecha(value):
    now = datetime.now()

    # custom validation: comprobamos que la fecha sea correcta.
    if value.year > now.year:
        raise serializers.ValidationError(INCORRECT_DATE)
    elif value.year == now.year and value.month > now.month:
        raise serializers.ValidationError(INCORRECT_DATE)
    elif value.year == now.year and value.month == now.month and value.day > now.day:
        raise serializers.ValidationError(INCORRECT_DATE)

def objeto_no_es_parte_del_grupo(value, grupo):
    # custom validation: comprobamos que el objeto dado sea parte de un grupo especifico.
    if value in grupo:
        return value
    raise serializers.ValidationError(INVALID_GROUP)        

def comprobar_espacio_vacio(value):
        # custom validation: comprobamos que el valor no este en blanco.
        if value == '':
            raise serializers.ValidationError(BLANK_SPACE)

#############################################[  Artist  ]############################################

class ListArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'ID': instance.id,
            'Nombre': instance.name,
            'Apellido': instance.last_name,
            'Nombre artistico': instance.artist_name,
        }


class DetailArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class CreateUpdateArtistSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    artist_name = serializers.CharField(max_length=100)

    class Meta:
        model = Artist
        fields = ('name', 'last_name', 'artist_name')

    def create(self, validated_data):
        artist = Artist(**validated_data)
        artist.save()
        return artist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.artist_name = validated_data.get('artist_name', instance.artist_name)
        instance.save()
        return instance

#############################################[  Album  ]#############################################

class ListAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):

        return {
            'ID': instance.id,
            'Titulo': instance.name,
            'Fecha de lanzamiento': instance.release_date,
            'Tapa': instance.image if instance.image != '' else '',
            'Artista': instance.belongs_to_artist.artist_name,
        }


class DetailAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class CreateUpdateAlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    release_date = serializers.DateField()
    genre = serializers.CharField(max_length=50)
    image = serializers.ImageField() 
    belongs_to_artist = ListArtistSerializer.Meta.model.objects.all().values('artist_name')

    class Meta:
        model = Album
        fields = ('name', 'release_date', 'genre', 'image', 'belongs_to_artist',)

    def validate_release_date(self, value):
        comprobar_fecha(value)
        return value

    def validate_genre(self, value):
        objeto_no_es_parte_del_grupo(value, GENRES)
        return value

    def validate_image(self, value):
        comprobar_espacio_vacio(value)
        return value

    def create(self, validated_data):
        album = Album(**validated_data)
        album.save()
        return album

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.image = validated_data.get('image', instance.image)
        instance.belongs_to_artist = validated_data.get('belongs_to_artist', instance.belongs_to_artist)
        instance.save()
        return instance


class AlbumImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'image')
        read_only_fields = ('id',)
