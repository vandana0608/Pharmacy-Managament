# Generated by Django 2.0.7 on 2019-10-06 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_group', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine_group',
            old_name='tax',
            new_name='taxes',
        ),
    ]
