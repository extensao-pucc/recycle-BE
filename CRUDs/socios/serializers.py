from rest_framework import serializers
from .models import Socios

# Serializers define the API representation.
class SociosSerializer(serializers.HyperlinkedModelSerializer):
    # data_de_admissao = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Socios
        fields = ['id','matricula', 'nome', 'data_de_nascimento', 'RG', 'data_emissao', 'local_emissao', 
        'orgao_expedidor', 'CPF', 'titulo_de_Eleitor', 'PIS_PASEP', 'NIT', 'nome_da_Mae', 'nome_do_Pai', 
        'endereco', 'numero', 'complemento', 'CEP', 'UF', 'cidade', 'telefone', 'email', 'data_de_admissao', 
        'data_de_demissao', 'situacao', 'foto', 'perfil', 'senha', 'key']