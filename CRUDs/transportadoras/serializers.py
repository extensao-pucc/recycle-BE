from rest_framework import serializers
from .models import Transportadoras

# Serializers define the API representation.
class TransportadorasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transportadoras
        fields = ['id','CNPJ_CPF', 'razao_social_nome', 'IE', 'endereco', 'numero', 'complemento', 
        'bairro', 'CEP', 'UF', 'cidade', 'telefone', 'email']