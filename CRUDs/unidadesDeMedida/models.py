from django.db import models


class UnidadesDeMedida(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(verbose_name='descricao', max_length=100)
    sigla = models.CharField(verbose_name='sigla', max_length=6)

    def __str__(self):
        return self.sigla + ' - ' + self.descricao

    class Meta:
        verbose_name_plural = "Unidades de Medida"
