# Generated by Django 2.2.5 on 2020-03-21 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0006_auto_20200321_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onetimepassword',
            old_name='phone_id',
            new_name='phone',
        ),
    ]
