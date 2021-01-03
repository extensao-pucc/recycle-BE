from django.db import models
from CRUDs.socios.models import Socios
from CRUDs.produtos.models import Produtos
from CRUDs.lote.models import Lote


class LoteItens(models.Model):
    id = models.AutoField(primary_key=True)
    num_lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING, verbose_name='Lote')
    num_recipiente = models.IntegerField(verbose_name='Numero do Recipiente')
    produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, verbose_name='Produtos')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    socio = models.ForeignKey(Socios, on_delete=models.DO_NOTHING, verbose_name='Socios')
    data_iniciado = models.DateField(verbose_name='Data Iniciado', blank=False)
    data_finalizado = models.DateField(verbose_name='Data Finalizado', blank=False)
    hora_iniciado = models.TimeField(verbose_name='Hora Iniciado', blank=False)
    hora_finalizado = models.TimeField(verbose_name='Hora Finalizado', blank=False)
    tempo_total = models.TimeField(verbose_name='Tempo Total', blank=False)

    def __str__(self):
        return self.num_lote

    class Meta:
        verbose_name_plural = "Itens do Lote"
