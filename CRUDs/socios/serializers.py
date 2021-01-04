from rest_framework import serializers
from .models import Socios

# Serializers define the API representation.
class SociosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Socios
        fields = ['id','matricula', 'nome', 'data_de_nascimento', 'RG', 'data_emissao', 'local_emissao', 
        'orgao_expedidor', 'CPF', 'titulo_de_Eleitor', 'PIS_PASEP', 'NIT', 'nome_da_Mae', 'nome_do_Pai', 
        'endereco', 'numero', 'complemento', 'UF', 'cidade', 'telefone', 'email', 'data_de_admissao', 
        'data_de_demissao', 'situacao', 'foto', 'perfil', 'senha']