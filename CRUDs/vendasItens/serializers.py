from rest_framework import serializers
from .models import VendasItens

# Serializers define the API representation.
class VendasItensSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendasItens
        fields = ['id','descricao']