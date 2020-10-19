from rest_framework import serializers
from .models import UnidadesDeMedida

# Serializers define the API representation.
class UnidadesDeMedidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadesDeMedida
        fields = ['id','sigla', 'descricao']