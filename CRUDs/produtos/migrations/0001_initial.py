# Generated by Django 3.1.2 on 2020-10-19 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('naturezaDasOperacoes', '0001_initial'),
        ('fornecedores', '0002_auto_20201018_2210'),
        ('unidadesDeMedida', '0001_initial'),
        ('qualidades', '0001_initial'),
        ('familias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('NCM', models.CharField(max_length=10, verbose_name='NCM')),
                ('CSTE', models.CharField(max_length=5, verbose_name='CSTE')),
                ('CSTS', models.CharField(max_length=5, verbose_name='CSTS')),
                ('preco_compra', models.CharField(max_length=100, verbose_name='Preço de Compra')),
                ('preco_venda', models.CharField(max_length=100, verbose_name='Preço de Venda')),
                ('CFOPE', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='CFOPE', to='naturezaDasOperacoes.naturezadasoperacoes')),
                ('CFOPS', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='CFOPS', to='naturezaDasOperacoes.naturezadasoperacoes')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='familias.familias', verbose_name='Famílias')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fornecedores.fornecedores', verbose_name='Fornecedores')),
                ('qualidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='qualidades.qualidades', verbose_name='Qualidades')),
                ('unidade_de_medida', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unidadesDeMedida.unidadesdemedida', verbose_name='Unidades de Medida')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]