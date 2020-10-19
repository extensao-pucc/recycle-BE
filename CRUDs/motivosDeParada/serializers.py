from rest_framework import serializers
from .models import MotivosDeParada

# Serializers define the API representation.
class MotivosDeParadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MotivosDeParada
        fields = ['id','motivo']