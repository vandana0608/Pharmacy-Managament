# Generated by Django 2.0.7 on 2019-10-13 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill_medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill_medicine',
            old_name='bill_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='bill_medicine',
            old_name='medicine_quantity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='bill_medicine',
            name='medicine_price',
        ),
    ]
