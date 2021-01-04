from django.db import models
from CRUDs.produtos.models import Produtos
from CRUDs.fornecedores.models import Fornecedores
from CRUDs.qualidades.models import Qualidades

class Valores(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, verbose_name='Produtos', related_name="valores_produto")
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores', related_name="valores_fornecedor")
    qualidade = models.ForeignKey(Qualidades, on_delete=models.DO_NOTHING, verbose_name='Qualidades', related_name="valores_qualidade")
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço de Compra')
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço de Venda')
   
    def __str__(self):
        return self.produto + ' - ' + self.fornecedor + ' - ' + self.qualidade
    
    class Meta:
        verbose_name_plural = "Valores"
