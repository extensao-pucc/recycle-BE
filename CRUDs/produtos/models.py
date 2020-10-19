from django.db import models
from CRUDs.familias.models import Familias
from CRUDs.fornecedores.models import Fornecedores
from CRUDs.qualidades.models import Qualidades
from CRUDs.naturezaDasOperacoes.models import NaturezaDasOperacoes
from CRUDs.unidadesDeMedida.models import UnidadesDeMedida


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    familia = models.ForeignKey(Familias, on_delete=models.DO_NOTHING, verbose_name='Famílias')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, verbose_name='Fornecedores')
    qualidade = models.ForeignKey(Qualidades, on_delete=models.DO_NOTHING, verbose_name='Qualidades')
    unidade_de_medida = models.ForeignKey(UnidadesDeMedida, on_delete=models.DO_NOTHING, verbose_name='Unidades de Medida')
    NCM = models.CharField(verbose_name='NCM', max_length=10)
    CSTE = models.CharField(verbose_name='CSTE', max_length=5)
    CSTS = models.CharField(verbose_name='CSTS', max_length=5)
    CFOPE = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPE')
    CFOPS = models.ForeignKey(NaturezaDasOperacoes, on_delete=models.DO_NOTHING, related_name='CFOPS')
    preco_compra = models.CharField(verbose_name='Preço de Compra', max_length=100)
    preco_venda = models.CharField(verbose_name='Preço de Venda', max_length=100)

    class Meta:
        verbose_name_plural = "Produtos"
