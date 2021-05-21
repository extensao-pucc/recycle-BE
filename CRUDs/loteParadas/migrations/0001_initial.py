# Generated by Django 3.1.2 on 2021-05-20 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('motivosDeParada', '0001_initial'),
        ('lote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoteParadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('finalizado', models.DateTimeField(verbose_name='Finalizado')),
                ('iniciado', models.DateTimeField(verbose_name='Iniciado')),
                ('sequencia', models.IntegerField(verbose_name='Sequencia')),
                ('tempo_total', models.IntegerField(verbose_name='Tempo Total')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='motivosDeParada.motivosdeparada', verbose_name='Motivos De Parada')),
                ('num_lote', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lote.lote', verbose_name='Lote')),
            ],
            options={
                'verbose_name_plural': 'Paradas do Lote',
            },
        ),
    ]
