# Generated by Django 3.1.2 on 2021-09-16 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('qualidades', '0001_initial'),
        ('produtos', '0001_initial'),
        ('precificacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='precificacao',
            unique_together={('fornecedor', 'qualidade', 'produto')},
        ),
    ]
