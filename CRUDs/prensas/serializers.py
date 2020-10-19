from rest_framework import serializers
from .models import Prensas

# Serializers define the API representation.
class PrensasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prensas
        fields = ['id','numero', 'descricao', 'detalhes_tecnicos']