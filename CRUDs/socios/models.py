from django.db import models
from PIL import Image
from django.conf import settings

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key.decode()

def encryptPassword(password, key):
    fernet = Fernet(key.encode())
    encryptPassw = fernet.encrypt(password.encode())
    return encryptPassw.decode()
    
class Socios(models.Model):
    id = models.AutoField(primary_key=True)
    cidade = models.CharField(verbose_name='Cidade', max_length=100)
    complemento = models.CharField(verbose_name='Complemento', max_length=100, blank=True)
    CEP = models.CharField(verbose_name='CEP', max_length=9)
    CPF = models.CharField(verbose_name='CPF', max_length=14, blank=False)
    data_de_admissao = models.DateField(verbose_name='Data de admissão', blank=False)
    data_de_demissao = models.DateField(verbose_name='Data de demissão', blank=True, null=True)
    data_de_nascimento = models.DateField(verbose_name='Data de nascimento', blank=False)
    data_emissao = models.DateField(verbose_name='Data de Emissão', blank=False)
    email = models.CharField(verbose_name='Email', max_length=100, blank=False)
    endereco = models.CharField(verbose_name='Endereço', max_length=100, blank=False)
    foto = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Foto')
    local_emissao = models.CharField(verbose_name='Local de Emissão', max_length=100, blank=False)
    matricula = models.IntegerField(verbose_name='Matrícula', unique=True, blank=False)
    NIT = models.CharField(verbose_name='NIT', max_length=14, blank=False)
    nome = models.CharField(verbose_name='Nome', max_length=100, blank=False)
    nome_da_Mae = models.CharField(verbose_name='Nome da Mãe', max_length=100, blank=False)
    nome_do_Pai = models.CharField(verbose_name='Nome do Pai', max_length=100, blank=True)
    numero = models.IntegerField(verbose_name='Numero', blank=False)
    orgao_expedidor = models.CharField(verbose_name='Órgão Expedidor', max_length=6, blank=False)
    perfil = models.CharField(verbose_name='Perfil', blank=False, max_length=20)
    PIS_PASEP = models.CharField(verbose_name='PIS/PASEP', max_length=14, blank=False)
    RG = models.CharField(verbose_name='RG', max_length=100, blank=False)
    senha = models.CharField(verbose_name='Senha', blank=True, max_length=200)
    key = models.CharField(verbose_name='Key', blank=True, max_length=50)
    situacao = models.CharField(verbose_name='Situação', blank=False, max_length=10)
    telefone = models.CharField(verbose_name='Telefone', max_length=100, blank=False)
    titulo_de_Eleitor = models.CharField(verbose_name='Titulo de Eleitor', max_length=14, blank=False)
    UF = models.CharField(verbose_name='UF', blank=False, max_length=2)


    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Sócios"
        
    def save (self, *args, **kwargs):
        self.key = generate_key()
        self.senha = encryptPassword(self.senha, self.key)
        super(Socios, self).save(*args, **kwargs)

    def my_save (self, *args, **kwargs):
        super(Socios, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):

    #     try:
    #         extensao = self.foto.name.rfind('.')
    #         self.foto.name = str(self.matricula) + self.foto.name[extensao:]

    #         super().save(*args, **kwargs)
            
    #         self.resize_image(self.foto.name, 800)
        
    #     except:
    #         self.foto = None
    #         super().save(*args, **kwargs)
               
    # @staticmethod
    # def resize_image(img_name, new_width):
        
    #     img_path = os.path.join(settings.MEDIA_ROOT, img_name)
    #     img = Image.open(img_path)

    #     width, height = img.size
    #     new_height = round((new_width * height) / width)

    #     if width <= new_width:
    #         img.close()
    #         return

    #     new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    #     new_img.save(
    #         img_path,
    #         optimize=True,
    #         quality=60,

    #     )
    #     new_img.close()
