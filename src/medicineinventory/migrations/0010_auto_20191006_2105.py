# Generated by Django 2.0.7 on 2019-10-06 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicineinventory', '0009_auto_20191006_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineinventory',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
