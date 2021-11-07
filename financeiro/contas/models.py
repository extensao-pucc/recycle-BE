from django.db import models

class Contas(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(verbose_name='Data', blank=False)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    tipo = models.CharField(verbose_name='Tipo', max_length=15, blank=False)
    situacao = models.CharField(verbose_name='Situação', max_length=15, blank=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Contas"