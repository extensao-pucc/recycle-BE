# Generated by Django 3.1.2 on 2021-08-14 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loteItens', '0001_initial'),
        ('socios', '0001_initial'),
        ('precificacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loteitens',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='precificacao.precificacao', verbose_name='Produtos'),
        ),
        migrations.AddField(
            model_name='loteitens',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.socios', verbose_name='Socios'),
        ),
    ]