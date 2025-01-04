# Generated by Django 5.1.4 on 2025-01-04 02:16

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0005_payment_name_alter_income_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 1, 1, 2, 16, 21, 963463, tzinfo=datetime.timezone.utc)),
        ),
    ]