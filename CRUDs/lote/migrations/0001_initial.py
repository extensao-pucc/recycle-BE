# Generated by Django 3.1.2 on 2021-01-22 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socios', '0001_initial'),
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_iniciado', models.DateField(verbose_name='Data Iniciado')),
                ('data_finalizado', models.DateField(verbose_name='Data Finalizado')),
                ('hora_iniciado', models.TimeField(verbose_name='Hora Iniciado')),
                ('hora_finalizado', models.TimeField(verbose_name='Hora Finalizado')),
                ('nao_processado', models.DecimalField(decimal_places=3, max_digits=4, verbose_name='Não Processado')),
                ('num_lote', models.IntegerField(unique=True, verbose_name='Numero do Lote')),
                ('observacao', models.CharField(max_length=200, verbose_name='Observação')),
                ('tempo_total', models.TimeField(verbose_name='Tempo Total')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fornecedores.fornecedores', verbose_name='Fornecedores')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.socios', verbose_name='Socios')),
            ],
            options={
                'verbose_name_plural': 'Lote',
            },
        ),
    ]
