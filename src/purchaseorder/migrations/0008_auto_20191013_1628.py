# Generated by Django 2.0.7 on 2019-10-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0007_auto_20191013_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='purchase_orderno',
            field=models.CharField(default='PRO', max_length=10, primary_key=True, serialize=False),
        ),
    ]
