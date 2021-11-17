from django.db import models
from financeiro.vendas.models import Vendas
from CRUDs.precificacao.models import Precificacao


class VendasItens(models.Model):
    id = models.AutoField(primary_key=True)
    venda = models.ForeignKey(Vendas, on_delete=models.DO_NOTHING, verbose_name="venda")
    precificacao = models.ForeignKey(Precificacao, on_delete=models.DO_NOTHING, verbose_name="precificacao", default='null')
    quantidade = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Quantidade', default=0)

    def __str__(self):
        return self.produto

    class Meta:
        verbose_name_plural = "Venda itens"
