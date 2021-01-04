from django.db import models
from PIL import Image
from django.conf import settings
import os

class Socios(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.IntegerField(verbose_name='Matrícula', unique=True, blank=False)
    nome = models.CharField(verbose_name='Nome', max_length=100, blank=False)
    data_de_nascimento = models.DateField(verbose_name='Data de nascimento', blank=False)
    RG = models.CharField(verbose_name='RG', max_length=100, blank=False)
    data_emissao = models.DateField(verbose_name='Data de Emissão', blank=False)
    local_emissao = models.CharField(verbose_name='Local de Emissão', max_length=100, blank=False)
    orgao_expedidor = models.CharField(verbose_name='Órgão Expedidor', max_length=6, blank=False)
    CPF = models.CharField(verbose_name='CPF', max_length=14, blank=False)
    titulo_de_Eleitor = models.CharField(verbose_name='Titulo de Eleitor', max_length=14, blank=False)
    PIS_PASEP = models.CharField(verbose_name='PIS/PASEP', max_length=14, blank=False)
    NIT = models.CharField(verbose_name='NIT', max_length=14, blank=False)
    nome_da_Mae = models.CharField(verbose_name='Nome da Mãe', max_length=100, blank=False)
    nome_do_Pai = models.CharField(verbose_name='Nome do Pai', max_length=100, blank=True)
    endereco = models.CharField(verbose_name='Endereço', max_length=100, blank=False)
    numero = models.IntegerField(verbose_name='Numero', blank=False)
    complemento = models.CharField(verbose_name='Complemento', max_length=100, blank=True)
    UF = models.CharField(verbose_name='UF', blank=False, max_length=2)
    cidade = models.CharField(verbose_name='Cidade', max_length=100)
    telefone = models.CharField(verbose_name='Telefone', max_length=100, blank=False)
    email = models.CharField(verbose_name='Email', max_length=100, blank=False)
    data_de_admissao = models.DateField(verbose_name='Data de admissão', auto_now_add=True, blank=False)
    data_de_demissao = models.DateField(verbose_name='Data de demissão', blank=True, null=True)
    situacao = models.CharField(verbose_name='Situação', blank=False, max_length=10)
    foto = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Foto')
    perfil = models.CharField(verbose_name='Perfil', blank=False, max_length=20)
    senha = models.CharField(verbose_name='Senha', blank=False, max_length=14)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Sócios"

    def save(self, *args, **kwargs):

        try:
            extensao = self.foto.name.rfind('.')
            self.foto.name = str(self.matricula) + self.foto.name[extensao:]

            super().save(*args, **kwargs)
            
            self.resize_image(self.foto.name, 800)
        
        except:
            self.foto = None
            super().save(*args, **kwargs)
               
    @staticmethod
    def resize_image(img_name, new_width):
        
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)

        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60,

        )
        new_img.close()
