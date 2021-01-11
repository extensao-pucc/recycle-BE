from django.db import models
from CRUDs.motivosDeParada.models import MotivosDeParada
from CRUDs.produtos.models import Produtos
from CRUDs.lote.models import Lote


class LoteParadas(models.Model):
    id = models.AutoField(primary_key=True)
    data_iniciado = models.DateField(verbose_name='Data Iniciado', blank=False)
    data_finalizado = models.DateField(verbose_name='Data Finalizado', blank=False)
    hora_iniciado = models.TimeField(verbose_name='Hora Iniciado', blank=False)
    hora_finalizado = models.TimeField(verbose_name='Hora Finalizado', blank=False)
    motivo = models.ForeignKey(MotivosDeParada, on_delete=models.DO_NOTHING, verbose_name='Motivos De Parada')
    num_lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING, verbose_name='Lote')
    sequencia = models.IntegerField(verbose_name='Sequencia')
    tempo_total = models.TimeField(verbose_name='Tempo Total', blank=False)

    def __str__(self):
        return self.num_lote

    class Meta:
        verbose_name_plural = "Paradas do Lote"
