from rest_framework import serializers
from .models import Familias

# Serializers define the API representation.
class FamiliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Familias
        fields = ['id','nome']