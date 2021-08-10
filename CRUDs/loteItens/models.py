from django.db import models
from CRUDs.socios.models import Socios
from CRUDs.precificacao.models import Precificacao
from CRUDs.lote.models import Lote

class LoteItens(models.Model):
    id = models.AutoField(primary_key=True)
    finalizado = models.DateTimeField(verbose_name='Finalizado', blank=False)
    iniciado = models.DateTimeField(verbose_name='Iniciado', blank=False)
    num_lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING, verbose_name='Lote')
    num_recipiente = models.IntegerField(verbose_name='Numero do Recipiente')
    produto = models.ForeignKey(Precificacao, on_delete=models.DO_NOTHING, verbose_name='Produtos')
    quantidade = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Quantidade')
    socio = models.ForeignKey(Socios, on_delete=models.DO_NOTHING, verbose_name='Socios')
    tempo_total = models.IntegerField(verbose_name='Tempo Total', blank=False)

    def __str__(self):
        return self.num_lote.num_lote

    class Meta:
        verbose_name_plural = "Itens do Lote"
