from rest_framework import serializers
from .models import Movimentacoes
from CRUDs.precificacao.serializers import PrecificacaoSerializer

# Serializers define the API representation.
class MovimentacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacoes
        fields = ['id','data', 'entrada_saida', 'tipo', 'numero_tipo', 'cod_produto', 'saldo_anterior', 'saldo_atual', 'dif']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cod_produto'] = PrecificacaoSerializer(instance.cod_produto).data
        
        return response 