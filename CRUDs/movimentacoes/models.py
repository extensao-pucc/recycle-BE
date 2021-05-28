from django.db import models
from CRUDs.produtos.models import Produtos


class Movimentacoes(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(verbose_name='Data', blank=False)
    entrada_saida = models.CharField(verbose_name='E/S', max_length=1, unique=True)
    tipo = models.CharField(verbose_name='Tipo', max_length=50, unique=True)
    numero_tipo = models.IntegerField(verbose_name='Numero do tipo')
    cod_produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, related_name='Produtos')
    qtd_movimentada = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Quantidade movimentada')
    saldo_atual = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Saldo atual')


    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Movimentações"
