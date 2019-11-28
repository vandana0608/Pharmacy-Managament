# Generated by Django 2.0.7 on 2019-10-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_id', models.CharField(default='MID', max_length=10)),
                ('type_of_medicine', models.CharField(default='xxx', max_length=25)),
                ('tax', models.DecimalField(decimal_places=2, default='00.00', max_digits=50)),
            ],
        ),
    ]
