from django.db import models
from CRUDs.socios.models import Socios
from CRUDs.fornecedores.models import Fornecedores


class Lote(models.Model):
    num_lote = models.IntegerField(verbose_name='Numero do Lote', primary_key=True)
    finalizado = models.DateTimeField(verbose_name='Finalizado', blank=False)
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores', blank=True, null=True)
    iniciado = models.DateTimeField(verbose_name='Iniciado', blank=False)
    observacao = models.CharField(verbose_name='Observação', max_length=200)
    socio = models.ForeignKey(Socios, on_delete=models.DO_NOTHING, verbose_name='Socios')
    tempo_total = models.IntegerField(verbose_name='Tempo Total', blank=False)
    # nao_processado = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Não processado')

    def __str__(self):
        return str(self.num_lote)

    class Meta:
        verbose_name_plural = "Lote"
