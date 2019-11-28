# Generated by Django 2.0.7 on 2019-09-15 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0004_remove_bill_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
