# Generated by Django 3.1.2 on 2021-11-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qualidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='nome')),
            ],
            options={
                'verbose_name_plural': 'Qualidade',
            },
        ),
    ]
