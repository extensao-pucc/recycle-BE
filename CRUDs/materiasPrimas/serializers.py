from rest_framework import serializers
from .models import MateriasPrimas

# Serializers define the API representation.
class MateriasPrimasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MateriasPrimas
        fields = ['id','nome']