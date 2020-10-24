from django.db import models
from CRUDs.motivosDeParada.models import MotivosDeParada
from CRUDs.produtos.models import Produtos
from CRUDs.lote.models import Lote


class LoteParadas(models.Model):
    id = models.AutoField(primary_key=True)
    num_lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING, verbose_name='Lote')
    motivo = models.ForeignKey(MotivosDeParada, on_delete=models.DO_NOTHING, verbose_name='Motivos De Parada')
    sequencia = models.IntegerField(verbose_name='Sequencia')
    tempo = models.IntegerField(verbose_name='Quantidade')

    def __str__(self):
        return self.num_lote

    class Meta:
        verbose_name_plural = "Paradas do Lote"
