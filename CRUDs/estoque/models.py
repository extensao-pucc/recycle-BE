from django.db import models
from CRUDs.produtos.models import Produtos
from CRUDs.fornecedores.models import Fornecedores
from CRUDs.qualidades.models import Qualidades

class Estoque(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, verbose_name='Produtos', related_name="produto")
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores', related_name="fornecedor")
    qualidade = models.ForeignKey(Qualidades, on_delete=models.DO_NOTHING, verbose_name='Qualidades', related_name="qualidade")
    quantidade = models.CharField(verbose_name='Quantidade', max_length=100, unique=True)


    def __str__(self):
        return self.cod_produto

    class Meta:
        verbose_name_plural = "Condições de Pagamento"
