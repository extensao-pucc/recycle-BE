from rest_framework import serializers
from .models import LoteItens

# Serializers define the API representation.
class LoteItensSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoteItens
        fields = ['id','num_lote', 'num_recipiente', 'produto', 'quantidade', 'socio', 'iniciado', 'finalizado', 'tempo_total']