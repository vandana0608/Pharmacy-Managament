# Generated by Django 2.0.7 on 2019-10-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_medicine', '0004_auto_20191013_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_medicine',
            name='invoice_no',
            field=models.CharField(default='INVNO', max_length=10, primary_key=True, serialize=False),
        ),
    ]
