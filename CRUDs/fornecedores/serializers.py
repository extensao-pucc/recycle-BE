from rest_framework import serializers
from .models import Fornecedores

# Serializers define the API representation.
class FornecedoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fornecedores
        fields = ['id','CNPJ_CPF','razao_social_nome','IE','endereco','numero',
            'complemento','bairro','CEP','UF','cidade','telefone','email']
