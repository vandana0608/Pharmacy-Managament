# Generated by Django 2.0.7 on 2019-10-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20190917_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount',
            new_name='payment_amount',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='purchase_order',
            new_name='purchase_orderno',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='paymentdetails',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_details',
            field=models.TextField(default='Cheque/DD/NEFT'),
        ),
    ]
