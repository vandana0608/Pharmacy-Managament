# Generated by Django 2.0.7 on 2019-10-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0007_auto_20190917_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='doctor_name',
            field=models.TextField(default='Dr.xxx'),
        ),
    ]
