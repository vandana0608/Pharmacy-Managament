# Generated by Django 2.0.7 on 2019-09-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='purchaseorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaseorder', models.CharField(default='1PRO', max_length=10)),
                ('quantity', models.PositiveIntegerField(default='1')),
                ('price', models.DecimalField(decimal_places=2, default='00000.00', max_digits=10000)),
            ],
        ),
    ]
