from rest_framework import serializers
from .models import Produtos
from CRUDs.familias.serializers import FamiliasSerializer
from CRUDs.unidadesDeMedida.serializers import UnidadesDeMedidaSerializer
from CRUDs.naturezaDasOperacoes.serializers import NaturezaDasOperacoesSerializer

# Serializers define the API representation.
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id','codigo', 'descricao', 'familia', 'unidade_de_medida', 'NCM', 'CSTE', 'CSTS', 'CFOPE', 'CFOPS']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['familia'] = FamiliasSerializer(instance.familia).data
        response['unidade_de_medida'] = UnidadesDeMedidaSerializer(instance.unidade_de_medida).data
        response['CFOPE'] = NaturezaDasOperacoesSerializer(instance.CFOPE).data
        response['CFOPS'] = NaturezaDasOperacoesSerializer(instance.CFOPS).data
        return response