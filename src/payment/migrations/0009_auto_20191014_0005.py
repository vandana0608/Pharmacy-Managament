# Generated by Django 2.0.7 on 2019-10-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20191013_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(),
        ),
    ]
