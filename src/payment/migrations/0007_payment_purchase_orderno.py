# Generated by Django 2.0.7 on 2019-10-13 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0007_auto_20191013_1600'),
        ('payment', '0006_remove_payment_purchase_orderno'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='purchase_orderno',
            field=models.ForeignKey(default='1PRO', on_delete=django.db.models.deletion.CASCADE, to='purchaseorder.purchaseorder'),
            preserve_default=False,
        ),
    ]
