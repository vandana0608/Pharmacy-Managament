# Generated by Django 2.0.7 on 2019-10-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20191006_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='logout',
            field=models.DateTimeField(),
        ),
    ]
