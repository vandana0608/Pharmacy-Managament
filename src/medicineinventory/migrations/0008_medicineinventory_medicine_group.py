# Generated by Django 2.0.7 on 2019-10-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicineinventory', '0007_auto_20191006_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicineinventory',
            name='medicine_group',
            field=models.CharField(default='xxx', max_length=20),
        ),
    ]
