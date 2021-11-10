# Generated by Django 3.1.2 on 2021-11-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaturezaDasOperacoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('descricao', models.CharField(default='', max_length=100, verbose_name='Descrição')),
                ('tipo', models.CharField(choices=[('Entrada', 'Entrada'), ('Saida', 'Saída')], max_length=10, verbose_name='Tipo(E/S)')),
            ],
            options={
                'verbose_name_plural': 'Natureza das Operações',
            },
        ),
    ]
