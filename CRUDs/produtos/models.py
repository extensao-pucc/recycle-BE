from django.db import models
from CRUDs.familias.models import Familias
from CRUDs.naturezaDasOperacoes.models import NaturezaDasOperacoes
from CRUDs.unidadesDeMedida.models import UnidadesDeMedida


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    familia = models.ForeignKey(Familias, on_delete=models.DO_NOTHING, verbose_name='Famílias', related_name="familia")
    unidade_de_medida = models.ForeignKey(UnidadesDeMedida, on_delete=models.DO_NOTHING, verbose_name='Unidades de Medida', related_name="unidade_de_medida")
    NCM = models.CharField(verbose_name='NCM', max_length=10)
    CSTE = models.CharField(verbose_name='CSTE', max_length=5)
    CSTS = models.CharField(verbose_name='CSTS', max_length=5)
    CFOPE = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPE')
    CFOPS = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPS')
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Produtos"
