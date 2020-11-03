from rest_framework import serializers
from .models import Produtos
from CRUDs.familias.serializers import FamiliasSerializer
from CRUDs.fornecedores.serializers import FornecedoresSerializer
from CRUDs.qualidades.serializers import QualidadesSerializer
from CRUDs.unidadesDeMedida.serializers import UnidadesDeMedidaSerializer
from CRUDs.naturezaDasOperacoes.serializers import NaturezaDasOperacoesSerializer

# Serializers define the API representation.
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id','codigo', 'descricao', 'familia', 'fornecedor', 'qualidade', 'unidade_de_medida', 'NCM', 'CSTE', 'CSTS', 'CFOPE', 'CFOPS', 'preco_compra', 'preco_venda']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['familia'] = FamiliasSerializer(instance.familia).data
        response['fornecedor'] = FornecedoresSerializer(instance.fornecedor).data
        response['qualidade'] = QualidadesSerializer(instance.qualidade).data
        response['unidade_de_medida'] = UnidadesDeMedidaSerializer(instance.unidade_de_medida).data
        response['CFOPE'] = NaturezaDasOperacoesSerializer(instance.CFOPE).data
        response['CFOPS'] = NaturezaDasOperacoesSerializer(instance.CFOPS).data
        return response