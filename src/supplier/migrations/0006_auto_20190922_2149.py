# Generated by Django 2.0.7 on 2019-09-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_auto_20190922_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_address',
            field=models.CharField(default='xxx', max_length=30),
        ),
    ]
