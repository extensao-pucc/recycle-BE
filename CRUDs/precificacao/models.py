from django.db import models
from CRUDs.fornecedores.models import Fornecedores
from CRUDs.qualidades.models import Qualidades
from CRUDs.produtos.models import Produtos


class Precificacao(models.Model):
    id = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, related_name="valores_fornecedor")
    quantidade = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Quantidade', default=0)
    qualidade = models.ForeignKey(Qualidades, on_delete=models.DO_NOTHING, related_name="valores_qualidade")
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço de Compra')
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço de Venda')
    produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, related_name="produto")
    
    def __str__(self):
        return self.produto.descricao
    
    class Meta:
        verbose_name_plural = "Precificacao"
        unique_together = ("fornecedor", "qualidade", "produto")
