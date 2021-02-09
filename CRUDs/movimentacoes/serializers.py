from rest_framework import serializers
from .models import Movimentacoes
from CRUDs.produtos.serializers import ProdutosSerializer

# Serializers define the API representation.
class MovimentacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacoes
        fields = ['id','data', 'entrada_saida', 'tipo', 'numero_tipo', 'cod_produto', 'qtd_movimentada', 'saldo_atual']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cod_produto'] = ProdutosSerializer(instance.cod_produto).data
        
        return response 