from django.db import models
from CRUD.familias.models import Familias
from CRUD.fornecedores.models import Fornecedores
from CRUD.qualidades.models import Qualidades
from CRUD.naturezaDasOperacoes.models import NaturezaDasOperacoes
from CRUD.unidadesDeMedida.models import UnidadesdeMedida


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    familia = models.ForeignKey(Familia, on_delete=models.DO_NOTHING, verbose_name='Família')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING, verbose_name='Fornecedor')
    qualidade = models.ForeignKey(Qualidade, on_delete=models.DO_NOTHING, verbose_name='Qualidade')
    unidade_de_medida = models.ForeignKey(UnidadesdeMedida, on_delete=models.DO_NOTHING, verbose_name='Unidade de Medida')
    NCM = models.CharField(verbose_name='NCM', max_length=10)
    CSTE = models.CharField(verbose_name='CSTE', max_length=5)
    CSTS = models.CharField(verbose_name='CSTS', max_length=5)
    CFOPE = models.ForeignKey(Natureza_das_Operacoes, on_delete=models.DO_NOTHING, related_name='CFOPE')
    CFOPS = models.ForeignKey(Natureza_das_Operacoes, on_delete=models.DO_NOTHING, related_name='CFOPS')
    preco_compra = models.CharField(verbose_name='Preço de Compra', max_length=100)
    preco_venda = models.CharField(verbose_name='Preço de Venda', max_length=100)

    class Meta:
        verbose_name_plural = "Produtos"
