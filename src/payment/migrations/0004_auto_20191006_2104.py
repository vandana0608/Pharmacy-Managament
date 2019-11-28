# Generated by Django 2.0.7 on 2019-10-06 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20191006_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='purchase_orderno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchaseorder.purchaseorder'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
