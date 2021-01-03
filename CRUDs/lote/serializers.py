from rest_framework import serializers
from .models import Lote

# Serializers define the API representation.
class LoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lote
        fields = ['id','num_lote', 'data_iniciado', 'data_finalizado', 'hora_iniciado', 'hora_finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao']