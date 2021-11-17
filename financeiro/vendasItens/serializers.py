from rest_framework import serializers
from .models import VendasItens
from financeiro.vendas.serializers import VendasSerializer
from CRUDs.precificacao.serializers import PrecificacaoSerializer

# Serializers define the API representation.
class VendasItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendasItens
        fields = ['id','venda','precificacao', 'quantidade']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['venda'] = VendasSerializer(instance.venda).data
        response['precificacao'] = PrecificacaoSerializer(instance.precificacao).data
        
        return response