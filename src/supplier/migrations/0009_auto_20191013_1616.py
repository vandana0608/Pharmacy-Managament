# Generated by Django 2.0.7 on 2019-10-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0008_auto_20191006_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='id',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_id',
            field=models.CharField(default='SID', max_length=10, primary_key=True, serialize=False),
        ),
    ]
