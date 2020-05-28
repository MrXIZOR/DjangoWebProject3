# Generated by Django 3.0.6 on 2020-05-28 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200528_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 28, 12, 4, 33, 61839), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 28, 12, 4, 33, 63839), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 28, 12, 4, 33, 60839), verbose_name='Дата'),
        ),
    ]