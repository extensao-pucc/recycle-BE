from django.db import models


class UnidadesDeMedida(models.Model):
    id = models.AutoField(primary_key=True)
    sigla = models.CharField(verbose_name='sigla', max_length=6)
    descricao = models.CharField(verbose_name='descricao', max_length=100)

    class Meta:
        verbose_name_plural = "Unidades de Medida"
