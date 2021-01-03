from django.db import models
from CRUDs.socios.models import Socios
from CRUDs.fornecedores.models import Fornecedores


class Lote(models.Model):
    id = models.AutoField(primary_key=True)
    num_lote = models.IntegerField(verbose_name='Numero do Lote', unique=True)
    data_iniciado = models.DateField(verbose_name='Data Iniciado', blank=False)
    data_finalizado = models.DateField(verbose_name='Data Finalizado', blank=False)
    hora_iniciado = models.TimeField(verbose_name='Hora Iniciado', blank=False)
    hora_finalizado = models.TimeField(verbose_name='Hora Finalizado', blank=False)
    tempo_total = models.TimeField(verbose_name='Tempo Total', blank=False)
    socio = models.ForeignKey(Socios, on_delete=models.DO_NOTHING, verbose_name='Socios')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores')
    observacao = models.CharField(verbose_name='Observação', max_length=200)
    nao_processado = models.DecimalField(verbose_name='Não Processado', max_digits=4, decimal_places=3)

    def __str__(self):
        return self.num_lote

    class Meta:
        verbose_name_plural = "Lote"
