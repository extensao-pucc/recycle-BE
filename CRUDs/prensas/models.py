from django.db import models


class Prensas(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    detalhes_tecnicos = models.CharField(verbose_name='Detalhes Técnicos', max_length=100)
    numero = models.IntegerField(verbose_name='Numero', unique=True, blank=False)

    def __int__(self):
        return self.numero + ' - ' + self.descricao

    class Meta:
        verbose_name_plural = "Prensas"