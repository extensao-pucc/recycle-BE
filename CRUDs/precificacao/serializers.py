from rest_framework import serializers
from .models import Precificacao
from CRUDs.fornecedores.serializers import FornecedoresSerializer
from CRUDs.produtos.serializers import ProdutosSerializer
from CRUDs.qualidades.serializers import QualidadesSerializer

# Serializers define the API representation.
class PrecificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precificacao
        fields = ['id', 'fornecedor', 'preco_compra', 'preco_venda', 'produto', 'quantidade', 'qualidade']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['fornecedor'] = FornecedoresSerializer(instance.fornecedor).data
        response['produto'] = ProdutosSerializer(instance.produto).data
        response['qualidade'] = QualidadesSerializer(instance.qualidade).data
        
        return response