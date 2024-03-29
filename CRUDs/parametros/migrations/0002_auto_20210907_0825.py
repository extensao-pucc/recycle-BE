# Generated by Django 3.1.2 on 2021-09-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='numero_proxima_NFE',
            field=models.CharField(default=0, max_length=100, verbose_name='Numero Próxima NFE'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='numero_proxima_NFS',
            field=models.CharField(default=0, max_length=100, verbose_name='Numero Próxima NFS'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='prensa',
            field=models.CharField(default=0, max_length=100, verbose_name='Prensa'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='remanufatura',
            field=models.CharField(default=0, max_length=100, verbose_name='Remanufatura'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='triagem',
            field=models.CharField(default=0, max_length=100, verbose_name='Triagem'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='unidade_de_medida',
            field=models.CharField(default=0, max_length=6, verbose_name='Unidade de medida'),
        ),
    ]
