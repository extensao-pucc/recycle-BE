from rest_framework import serializers
from .models import Vendas

# Serializers define the API representation.
class VendasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendas
        fields = ['id','descricao']