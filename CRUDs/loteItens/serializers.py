from rest_framework import serializers
from .models import LoteItens
from CRUDs.lote.serializers import LoteSerializer
from CRUDs.socios.serializers import SociosSerializer

# Serializers define the API representation.
class LoteItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteItens
        fields = ['id','num_lote', 'num_recipiente', 'produto', 'quantidade', 'socio', 'iniciado', 'finalizado', 'tempo_total']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['num_lote'] = LoteSerializer(instance.num_lote).data
        response['socio'] = SociosSerializer(instance.socio).data
        
        return response