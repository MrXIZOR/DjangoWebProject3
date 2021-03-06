# Generated by Django 3.0.6 on 2020-05-27 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200527_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('topic', models.CharField(max_length=100, verbose_name='Тема сообщения')),
                ('category', models.TextField(verbose_name='Категория вопроса')),
                ('answer', models.TextField(verbose_name='Получить ответ?')),
                ('email', models.EmailField(max_length=30, verbose_name='Ваш e-mail')),
                ('message', models.TextField(verbose_name='Описание вопроса')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 27, 17, 1, 16, 79436), verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Сообщения по обратной связи',
                'db_table': 'Feedbacks',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 27, 17, 1, 16, 82436), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 27, 17, 1, 16, 91436), verbose_name='Дата'),
        ),
    ]
