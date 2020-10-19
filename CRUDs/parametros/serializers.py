from rest_framework import serializers
from .models import Parametros

# Serializers define the API representation.
class ParametrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametros
        fields = ['id','triagem', 'prensa', 'remanufatura', 'numero_proxima_NFE', 'numero_proxima_NFS']