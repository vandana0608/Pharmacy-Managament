# Generated by Django 2.0.7 on 2019-10-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0010_auto_20191013_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_no',
            field=models.CharField(default='BNO', max_length=10, primary_key=True, serialize=False),
        ),
    ]
