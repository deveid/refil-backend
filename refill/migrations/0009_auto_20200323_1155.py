# Generated by Django 2.2.5 on 2020-03-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0008_onetimepassword_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='used',
            field=models.BooleanField(null=True),
        ),
    ]
