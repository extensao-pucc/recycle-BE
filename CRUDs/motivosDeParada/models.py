from django.db import models


class MotivosDeParada(models.Model):
    id = models.AutoField(primary_key=True)
    motivo = models.CharField(verbose_name='Motivo', max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.motivo

    class Meta:
        verbose_name_plural = "Motivos de Parada"
