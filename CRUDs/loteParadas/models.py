from django.db import models
from CRUDs.motivosDeParada.models import MotivosDeParada
from CRUDs.produtos.models import Produtos
from CRUDs.lote.models import Lote


class LoteParadas(models.Model):
    id = models.AutoField(primary_key=True)
    finalizado = models.DateTimeField(verbose_name='Finalizado', blank=False)
    iniciado = models.DateTimeField(verbose_name='Iniciado', blank=False)
    motivo = models.ForeignKey(MotivosDeParada, on_delete=models.DO_NOTHING, verbose_name='Motivos De Parada')
    num_lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING, verbose_name='Lote')
    sequencia = models.IntegerField(verbose_name='Sequencia')
    tempo_total = models.IntegerField(verbose_name='Tempo Total', blank=False)

    def __str__(self):
        return self.num_lote.num_lote

    class Meta:
        verbose_name_plural = "Paradas do Lote"
