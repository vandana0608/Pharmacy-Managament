# Generated by Django 2.0.7 on 2019-10-06 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20191006_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 6, 17, 9, 6, 979806)),
        ),
        migrations.AlterField(
            model_name='login',
            name='logout',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 6, 17, 9, 6, 979806)),
        ),
    ]
