from rest_framework import serializers
from .models import Qualidades

# Serializers define the API representation.
class QualidadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Qualidades
        fields = ['id','nome']