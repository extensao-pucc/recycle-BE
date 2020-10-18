from django.db import models


class Qualidades(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(verbose_name='nome', max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Qualidade"