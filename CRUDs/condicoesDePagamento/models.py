from django.db import models


class CondicoesDePagamento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100, unique=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Condições de Pagamento"
