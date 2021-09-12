from rest_framework import serializers
from .models import Clientes

# Serializers define the API representation.
class ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clientes
        fields = ['id','CNPJ_CPF','razao_social_nome','endereco','numero',
            'complemento','bairro','CEP','UF','cidade','telefone','email']