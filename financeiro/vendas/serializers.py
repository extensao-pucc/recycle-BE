from rest_framework import serializers
from .models import Vendas
from CRUDs.clientes.serializers import ClientesSerializer
from CRUDs.condicoesDePagamento.serializers import CondicoesDePagamentoSerializer
from CRUDs.socios.serializers import SociosSerializer


# Serializers define the API representation.
class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas
        fields = ['id','cliente','data', 'forma_de_pagamento', 'valor', 'vendedor']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cliente'] = ClientesSerializer(instance.cliente).data
        response['forma_de_pagamento'] = CondicoesDePagamentoSerializer(instance.forma_de_pagamento).data
        response['vendedor'] = SociosSerializer(instance.vendedor).data
        
        return response