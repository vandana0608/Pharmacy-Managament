# Generated by Django 2.0.7 on 2019-11-15 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicineinventory', '0018_auto_20191115_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineinventory',
            name='supplier_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
