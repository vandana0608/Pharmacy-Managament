# Generated by Django 2.0.7 on 2019-10-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0003_auto_20191006_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='shipment_address',
            field=models.TextField(default=25),
        ),
    ]
