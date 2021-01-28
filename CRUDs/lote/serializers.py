from rest_framework import serializers
from .models import Lote

# Serializers define the API representation.
class LoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lote
        fields = ['id','num_lote', 'iniciado', 'finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao']