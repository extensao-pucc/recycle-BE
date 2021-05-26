# Generated by Django 3.1.2 on 2021-05-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MateriasPrimas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Materias Primas',
            },
        ),
    ]
