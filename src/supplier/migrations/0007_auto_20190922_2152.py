# Generated by Django 2.0.7 on 2019-09-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0006_auto_20190922_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_id',
            field=models.CharField(default='SID', max_length=10),
        ),
    ]
