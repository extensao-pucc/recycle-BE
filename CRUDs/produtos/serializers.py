from rest_framework import serializers
from .models import Produtos
from CRUDs.familias.serializers import FamiliasSerializer
from CRUDs.naturezaDasOperacoes.serializers import NaturezaDasOperacoesSerializer

# Serializers define the API representation.
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id','codigo', 'descricao', 'familia', 'NCM', 'CSTE', 'CSTS', 'CFOPE', 'CFOPS']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['CFOPE'] = NaturezaDasOperacoesSerializer(instance.CFOPE).data
        response['CFOPS'] = NaturezaDasOperacoesSerializer(instance.CFOPS).data
        response['familia'] = FamiliasSerializer(instance.familia).data
        
        return response