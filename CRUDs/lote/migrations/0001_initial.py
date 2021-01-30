# Generated by Django 3.1.2 on 2021-01-29 23:49

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
                ('num_lote', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero do Lote')),
                ('finalizado', models.DateTimeField(verbose_name='Finalizado')),
                ('iniciado', models.DateTimeField(verbose_name='Iniciado')),
                ('observacao', models.CharField(max_length=200, verbose_name='Observação')),
                ('tempo_total', models.IntegerField(verbose_name='Tempo Total')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fornecedores.fornecedores', verbose_name='Fornecedores')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.socios', verbose_name='Socios')),
            ],
            options={
                'verbose_name_plural': 'Lote',
            },
        ),
    ]
