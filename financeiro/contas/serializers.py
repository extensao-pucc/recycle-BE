from rest_framework import serializers
from .models import Contas


class ContasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contas
        fields = ['id', 'descricao', 'data', 'tipo', 'valor', 'situacao']