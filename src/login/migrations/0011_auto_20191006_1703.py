# Generated by Django 2.0.7 on 2019-10-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_login_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login',
            field=models.DateTimeField(),
        ),
    ]
