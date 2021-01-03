# Generated by Django 3.1.2 on 2021-01-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matrícula')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('RG', models.CharField(max_length=100, verbose_name='RG')),
                ('data_emissao', models.DateField(verbose_name='Data de Emissão')),
                ('local_emissao', models.CharField(max_length=100, verbose_name='Local de Emissão')),
                ('orgao_expedidor', models.CharField(max_length=6, verbose_name='Órgão Expedidor')),
                ('CPF', models.CharField(max_length=14, verbose_name='CPF')),
                ('titulo_de_Eleitor', models.CharField(max_length=14, verbose_name='Titulo de Eleitor')),
                ('PIS_PASEP', models.CharField(max_length=14, verbose_name='PIS/PASEP')),
                ('NIT', models.CharField(max_length=14, verbose_name='NIT')),
                ('nome_da_Mae', models.CharField(max_length=100, verbose_name='Nome da Mãe')),
                ('nome_do_Pai', models.CharField(blank=True, max_length=100, verbose_name='Nome do Pai')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('UF', models.CharField(max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('data_de_admissao', models.DateField(auto_now_add=True, verbose_name='Data de admissão')),
                ('data_de_demissao', models.DateField(blank=True, null=True, verbose_name='Data de demissão')),
                ('situacao', models.CharField(max_length=10, verbose_name='Situação')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Foto')),
                ('perfil', models.CharField(max_length=20, verbose_name='Perfil')),
            ],
            options={
                'verbose_name_plural': 'Sócios',
            },
        ),
    ]
