# Generated by Django 3.1.2 on 2020-10-24 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_lote', models.IntegerField(unique=True, verbose_name='Numero do Lote')),
                ('iniciado', models.DateField(verbose_name='Iniciado')),
                ('finalizado', models.DateField(verbose_name='Iniciado')),
                ('observacao', models.CharField(max_length=200, verbose_name='Observação')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fornecedores.fornecedores', verbose_name='Fornecedores')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.socios', verbose_name='Socios')),
            ],
            options={
                'verbose_name_plural': 'Lote',
            },
        ),
    ]
