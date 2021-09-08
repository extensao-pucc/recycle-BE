# Generated by Django 3.1.2 on 2021-09-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_auto_20210907_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='numero_proxima_NFE',
            field=models.CharField(max_length=100, verbose_name='Numero Próxima NFE'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='numero_proxima_NFS',
            field=models.CharField(max_length=100, verbose_name='Numero Próxima NFS'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='prensa',
            field=models.CharField(max_length=100, verbose_name='Prensa'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='remanufatura',
            field=models.CharField(max_length=100, verbose_name='Remanufatura'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='triagem',
            field=models.CharField(max_length=100, verbose_name='Triagem'),
        ),
        migrations.AlterField(
            model_name='parametros',
            name='unidade_de_medida',
            field=models.CharField(max_length=6, verbose_name='Unidade de medida'),
        ),
    ]