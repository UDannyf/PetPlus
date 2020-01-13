from .models import *
from rest_framework import serializers


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ('localdireccion', 'localtelefono', 'localmail')

class RazaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raza
        fields = ('idraza', 'razanombre', 'razadescripcion')

class TipoMascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoMascota
        fields = ('idtipo', 'nombretipo', 'descripciontipo')
