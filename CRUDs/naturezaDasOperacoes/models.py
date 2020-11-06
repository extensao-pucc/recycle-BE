from django.db import models


class NaturezaDasOperacoes(models.Model):
    tipos=[
        ('Entrada', 'Entrada'),
        ('Saida', 'Saída'),
    ]

    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(verbose_name='Código', unique=True, blank=False)
    descricao = models.CharField(verbose_name='Descrição', default="", max_length=100, blank=False)
    tipo = models.CharField(verbose_name='Tipo(E/S)', max_length=10, blank=False, choices=tipos)

    def __int__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Natureza das Operações"
