# Generated by Django 2.0.7 on 2019-09-17 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_auto_20190915_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='emailid',
            new_name='email_id',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='address',
            new_name='supplier_address',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='supplierphonenumber',
            new_name='supplier_contactno',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='supplierid',
            new_name='supplier_id',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='suppliername',
            new_name='supplier_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='medicinedealership',
        ),
    ]
