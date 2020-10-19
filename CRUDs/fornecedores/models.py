from django.db import models


class Fornecedores(models.Model):
    estados = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    id = models.AutoField(primary_key=True)
    CNPJ_CPF = models.CharField(verbose_name='CNPJ/CPF', max_length=18, unique=True, blank=False)
    razao_social_nome = models.CharField(verbose_name='Razão Social/Nome', max_length=100)
    IE = models.CharField(verbose_name='IE', max_length=9)
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.IntegerField(verbose_name='Numero')
    complemento = models.CharField(verbose_name='Complemento', max_length=50, blank=True)
    bairro = models.CharField(verbose_name='Bairro', max_length=100)
    CEP = models.CharField(verbose_name='CEP', max_length=9)
    UF = models.CharField(verbose_name='UF', blank=False, max_length=10, choices=estados)
    cidade = models.CharField(verbose_name='Cidade', max_length=100)
    fone = models.CharField(verbose_name='Fone', max_length=16)
    email = models.CharField(verbose_name='Email', max_length=100)

    def __str__(self):
        return self.razao_social_nome

    class Meta:
        verbose_name_plural = "Fornecedores"
