# Generated by Django 2.2.5 on 2020-03-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0009_auto_20200323_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(blank=True, default='080389898043', help_text='Field to save the phone number of the user.', max_length=15, verbose_name='phone number'),
            preserve_default=False,
        ),
    ]
