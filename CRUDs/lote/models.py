from django.db import models
from CRUDs.socios.models import Socios
from CRUDs.fornecedores.models import Fornecedores


class Lote(models.Model):
    id = models.AutoField(primary_key=True)
    num_lote = models.IntegerField(verbose_name='Numero do Lote', unique=True)
    iniciado = models.DateField(verbose_name='Iniciado', blank=False)
    finalizado = models.DateField(verbose_name='Iniciado', blank=False)
    socio = models.ForeignKey(Socios, on_delete=models.DO_NOTHING, verbose_name='Socios')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores')
    observacao = models.CharField(verbose_name='Observação', max_length=200)

    def __str__(self):
        return self.num_lote

    class Meta:
        verbose_name_plural = "Lote"
