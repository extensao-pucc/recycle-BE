from rest_framework import serializers
from .models import LoteParadas

# Serializers define the API representation.
class LoteParadasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoteParadas
        fields = ['id','num_lote', 'motivo', 'sequencia', 'iniciado', 'finalizado', 'tempo_total']
