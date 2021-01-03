# Generated by Django 3.1.2 on 2021-01-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prensas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField(unique=True, verbose_name='Numero')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('detalhes_tecnicos', models.CharField(max_length=100, verbose_name='Detalhes Técnicos')),
            ],
            options={
                'verbose_name_plural': 'Prensas',
            },
        ),
    ]
