from rest_framework import serializers
from .models import Estoque
from CRUDs.fornecedores.serializers import FornecedoresSerializer
from CRUDs.qualidades.serializers import QualidadesSerializer
from CRUDs.produtos.serializers import ProdutosSerializer

# Serializers define the API representation.
class EstoqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estoque
        fields = ['id','produto','fornecedor','qualidade','quantidade']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['fornecedor'] = FornecedoresSerializer(instance.fornecedor).data
        response['qualidade'] = QualidadesSerializer(instance.qualidade).data
        response['produtos'] = ProdutosSerializer(instance.produto).data
        return response