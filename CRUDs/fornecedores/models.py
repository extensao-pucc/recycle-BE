from django.db import models


class Fornecedores(models.Model):

    id = models.AutoField(primary_key=True)
    CNPJ_CPF = models.CharField(verbose_name='CNPJ ou CPF', max_length=18, unique=True, blank=False)
    razao_social_nome = models.CharField(verbose_name='Razão social ou Nome', max_length=100)
    IE = models.CharField(verbose_name='IE', max_length=9)
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.IntegerField(verbose_name='Numero')
    complemento = models.CharField(verbose_name='Complemento', max_length=50, blank=True)
    bairro = models.CharField(verbose_name='Bairro', max_length=100)
    CEP = models.CharField(verbose_name='CEP', max_length=9)
    UF = models.CharField(verbose_name='UF', blank=False, max_length=2)
    cidade = models.CharField(verbose_name='Cidade', max_length=100)
    telefone = models.CharField(verbose_name='Telefone', max_length=16)
    email = models.CharField(verbose_name='Email', max_length=100)

    def __str__(self):
        return self.razao_social_nome + ' - ' + self.CNPJ_CPF

    class Meta:
        verbose_name_plural = "Fornecedores"
