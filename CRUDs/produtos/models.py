from django.db import models
from CRUDs.familias.models import Familias
from CRUDs.naturezaDasOperacoes.models import NaturezaDasOperacoes


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    CFOPE = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPE')
    CFOPS = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPS')
    CSTE = models.CharField(verbose_name='CSTE', max_length=5)
    CSTS = models.CharField(verbose_name='CSTS', max_length=5)
    familia = models.ForeignKey(Familias, on_delete=models.DO_NOTHING, verbose_name='Famílias', related_name="familia")
    NCM = models.CharField(verbose_name='NCM', max_length=10)
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Produtos"
