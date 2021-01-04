from rest_framework import serializers
from .models import Valores
from CRUDs.fornecedores.serializers import FornecedoresSerializer
from CRUDs.produtos.serializers import ProdutosSerializer
from CRUDs.qualidades.serializers import QualidadesSerializer

# Serializers define the API representation.
class ValoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valores
        fields = ['id', 'produto', 'fornecedor', 'qualidade', 'preco_compra', 'preco_venda']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['produto'] = ProdutosSerializer(instance.produto).data
        response['fornecedor'] = FornecedoresSerializer(instance.fornecedor).data
        response['qualidade'] = QualidadesSerializer(instance.qualidade).data

        return response