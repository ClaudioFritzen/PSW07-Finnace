# Generated by Django 4.2.3 on 2023-07-18 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
