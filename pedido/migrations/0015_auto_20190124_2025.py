# Generated by Django 2.0.10 on 2019-01-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0014_auto_20190124_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='quantidade',
            field=models.FloatField(default=0),
        ),
    ]
