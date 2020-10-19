from rest_framework import serializers
from .models import Produtos

# Serializers define the API representation.
class ProdutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id','codigo', 'descricao', 'familia', 'fornecedor', 'qualidade', 'unidade_de_medida', 'NCM', 'CSTE', 'CSTS', 'CFOPE', 'CFOPS', 'preco_compra', 'preco_venda']