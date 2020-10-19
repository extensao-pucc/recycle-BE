from rest_framework import serializers
from .models import NaturezaDasOperacoes

# Serializers define the API representation.
class NaturezaDasOperacoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NaturezaDasOperacoes
        fields = ['id','codigo', 'descricao', 'tipo']