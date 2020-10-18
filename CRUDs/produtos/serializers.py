from rest_framework import serializers
from .models import CondicoesDePagamento

# Serializers define the API representation.
class CondicoesDePagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CondicoesDePagamento
        fields = ['id','descricao']