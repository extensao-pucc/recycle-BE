from rest_framework import serializers
from .models import Produtos
from CRUDs.familias.serializers import FamiliasSerializer
from CRUDs.fornecedores.serializers import FornecedoresSerializer
from CRUDs.qualidades.serializers import QualidadesSerializer
from CRUDs.unidadesDeMedida.serializers import UnidadesDeMedidaSerializer
from CRUDs.naturezaDasOperacoes.serializers import NaturezaDasOperacoesSerializer

# Serializers define the API representation.
class ProdutosSerializer(serializers.HyperlinkedModelSerializer):
    familia = FamiliasSerializer(many=False)
    fornecedor = FornecedoresSerializer(many=False)
    qualidade = QualidadesSerializer(many=False)
    unidade_de_medida = UnidadesDeMedidaSerializer(many=False)
    CFOPE = NaturezaDasOperacoesSerializer(many=False)
    CFOPS = NaturezaDasOperacoesSerializer(many=False)
    class Meta:
        model = Produtos
        fields = ['id','codigo', 'descricao', 'familia', 'fornecedor', 'qualidade', 'unidade_de_medida', 'NCM', 'CSTE', 'CSTS', 'CFOPE', 'CFOPS', 'preco_compra', 'preco_venda']