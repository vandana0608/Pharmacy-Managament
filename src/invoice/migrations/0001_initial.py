# Generated by Django 2.0.7 on 2019-09-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceno', models.CharField(default='1INV', max_length=10)),
                ('date', models.DateField()),
                ('invoicevalue', models.PositiveIntegerField(default='0')),
                ('items', models.CharField(default='xxx', max_length=25)),
                ('price', models.DecimalField(decimal_places=2, default='00000.00', max_digits=10000)),
                ('taxes', models.DecimalField(decimal_places=2, default='00.00', max_digits=50)),
            ],
        ),
    ]
