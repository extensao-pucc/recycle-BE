from django.db import models


class Parametros(models.Model):
    id = models.AutoField(primary_key=True)
    numero_proxima_NFE = models.CharField(verbose_name='Numero Próxima NFE', max_length=100)
    numero_proxima_NFS = models.CharField(verbose_name='Numero Próxima NFS', max_length=100)
    prensa = models.CharField(verbose_name='Prensa', max_length=100, blank=False)
    remanufatura = models.CharField(verbose_name='Remanufatura', max_length=100, blank=False)
    triagem = models.CharField(verbose_name='Triagem', max_length=100, blank=False)
    unidade_de_medida = models.CharField(verbose_name='Unidade de medida', max_length=6)

    class Meta:
        verbose_name_plural = "Parâmetros"