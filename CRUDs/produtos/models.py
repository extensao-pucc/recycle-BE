from django.db import models
from CRUDs.familias.models import Familias
from CRUDs.fornecedores.models import Fornecedores
from CRUDs.naturezaDasOperacoes.models import NaturezaDasOperacoes
from CRUDs.qualidades.models import Qualidades
from CRUDs.unidadesDeMedida.models import UnidadesDeMedida


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    CFOPE = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPE')
    CFOPS = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPS')
    CSTE = models.CharField(verbose_name='CSTE', max_length=5)
    CSTS = models.CharField(verbose_name='CSTS', max_length=5)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    familia = models.ForeignKey(Familias, on_delete=models.DO_NOTHING, verbose_name='Famílias', related_name="familia")
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores', related_name="valores_fornecedor")
    NCM = models.CharField(verbose_name='NCM', max_length=10)
    quantidade = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Quantidade', default=0)
    qualidade = models.ForeignKey(Qualidades, on_delete=models.DO_NOTHING, verbose_name='Qualidades', related_name="valores_qualidade")
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço de Compra')
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço de Venda')
    unidade_de_medida = models.ForeignKey(UnidadesDeMedida, on_delete=models.DO_NOTHING, verbose_name='Unidades de Medida', related_name="unidade_de_medida")
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Produtos"
