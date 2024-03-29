# Generated by Django 3.1.2 on 2021-06-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transportadoras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('CEP', models.CharField(max_length=100, verbose_name='CEP')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('CNPJ_CPF', models.CharField(max_length=18, unique=True, verbose_name='CNPJ ou CPF')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('IE', models.CharField(max_length=100, verbose_name='IE')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('razao_social_nome', models.CharField(max_length=100, verbose_name='Razão social ou Nome')),
                ('telefone', models.CharField(max_length=16, verbose_name='Telefone')),
                ('UF', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name_plural': 'Transportadoras',
            },
        ),
    ]
