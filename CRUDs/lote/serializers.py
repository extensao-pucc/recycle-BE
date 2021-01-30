from rest_framework import serializers
from .models import Lote
from CRUDs.fornecedores.serializers import FornecedoresSerializer
from CRUDs.socios.serializers import SociosSerializer


# Serializers define the API representation.
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['num_lote', 'iniciado', 'finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao']
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['fornecedor'] = FornecedoresSerializer(instance.fornecedor).data
        response['socio'] = SociosSerializer(instance.socio).data
        
        return response