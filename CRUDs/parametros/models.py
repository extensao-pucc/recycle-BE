from django.db import models


class Parametros(models.Model):
    id = models.AutoField(primary_key=True)
    numero_proxima_NFE = models.CharField(verbose_name='Numero Próxima NFE', max_length=100, blank=True)
    numero_proxima_NFS = models.CharField(verbose_name='Numero Próxima NFS', max_length=100, blank=True)
    prensa = models.CharField(verbose_name='Prensa', max_length=100, blank=True)
    remanufatura = models.CharField(verbose_name='Remanufatura', max_length=100, blank=True)
    triagem = models.CharField(verbose_name='Triagem', max_length=100, blank=True)
    unidade_de_medida = models.CharField(verbose_name='Unidade de medida', max_length=6, blank=True)

    class Meta:
        verbose_name_plural = "Parâmetros"