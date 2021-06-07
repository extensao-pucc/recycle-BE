# Generated by Django 3.1.2 on 2021-06-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotivosDeParada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=100, unique=True, verbose_name='Motivo')),
            ],
            options={
                'verbose_name_plural': 'Motivos de Parada',
            },
        ),
    ]
