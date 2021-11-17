from django.db import models
from CRUDs.clientes.models import Clientes
from CRUDs.condicoesDePagamento.models import CondicoesDePagamento
from CRUDs.socios.models import Socios


class Vendas(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING, related_name="cliente")
    data = models.DateField(verbose_name='Data', auto_now_add=True, blank=False)
    forma_de_pagamento = models.ForeignKey(CondicoesDePagamento, on_delete=models.DO_NOTHING, related_name="forma_de_pagamento")
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor', default=0)
    vendedor = models.ForeignKey(Socios, on_delete=models.DO_NOTHING, related_name="vendedor")
    
    def __str__(self):
        return self.cliente.razao_social_nome

    class Meta:
        verbose_name_plural = "Venda"
