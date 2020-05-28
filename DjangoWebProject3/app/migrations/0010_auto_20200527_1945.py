# Generated by Django 3.0.6 on 2020-05-27 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200527_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 27, 19, 45, 14, 700172), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 27, 19, 45, 14, 702173), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 27, 19, 45, 14, 698172), verbose_name='Дата'),
        ),
    ]