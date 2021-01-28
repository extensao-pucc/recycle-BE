# Generated by Django 3.1.2 on 2021-01-28 23:16

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
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('CEP', models.CharField(max_length=9, verbose_name='CEP')),
                ('CPF', models.CharField(max_length=14, verbose_name='CPF')),
                ('data_de_admissao', models.DateField(auto_now_add=True, verbose_name='Data de admissão')),
                ('data_de_demissao', models.DateField(blank=True, null=True, verbose_name='Data de demissão')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('data_emissao', models.DateField(verbose_name='Data de Emissão')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Foto')),
                ('local_emissao', models.CharField(max_length=100, verbose_name='Local de Emissão')),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matrícula')),
                ('NIT', models.CharField(max_length=14, verbose_name='NIT')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_da_Mae', models.CharField(max_length=100, verbose_name='Nome da Mãe')),
                ('nome_do_Pai', models.CharField(blank=True, max_length=100, verbose_name='Nome do Pai')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('orgao_expedidor', models.CharField(max_length=6, verbose_name='Órgão Expedidor')),
                ('perfil', models.CharField(max_length=20, verbose_name='Perfil')),
                ('PIS_PASEP', models.CharField(max_length=14, verbose_name='PIS/PASEP')),
                ('RG', models.CharField(max_length=100, verbose_name='RG')),
                ('senha', models.CharField(blank=True, max_length=14, verbose_name='Senha')),
                ('situacao', models.CharField(max_length=10, verbose_name='Situação')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('titulo_de_Eleitor', models.CharField(max_length=14, verbose_name='Titulo de Eleitor')),
                ('UF', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name_plural': 'Sócios',
            },
        ),
    ]
