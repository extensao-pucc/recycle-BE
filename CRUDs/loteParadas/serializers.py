from rest_framework import serializers
from .models import LoteParadas
from CRUDs.lote.serializers import LoteSerializer
from CRUDs.motivosDeParada.serializers import MotivosDeParadaSerializer

# Serializers define the API representation.
class LoteParadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteParadas
        fields = ['id','num_lote', 'motivo', 'sequencia', 'iniciado', 'finalizado', 'tempo_total']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['num_lote'] = LoteSerializer(instance.num_lote).data
        response['motivo'] = MotivosDeParadaSerializer(instance.motivo).data
        
        return response 