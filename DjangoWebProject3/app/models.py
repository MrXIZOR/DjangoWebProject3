"""
Definition of models.
"""


from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import admin
from django.urls import reverse

class Feedback(models.Model):
    CATEGORIES = (
        ('1','Ошибка'),
        ('2', 'Блог'),
        ('3', 'Авторские права')
    )

    name = models.CharField(max_length = 100, verbose_name = "Имя")
    topic = models.CharField(verbose_name='Тема сообщения', max_length=100)
    category = models.CharField(verbose_name='Категория вопроса',
                                 choices=CATEGORIES, max_length=1)
    answer = models.BooleanField(verbose_name="Получить ответ?", default=False)
    #answer = models.CharField(verbose_name="Получить ответ?", max_length=3)
    email = models.EmailField(verbose_name='Электронная почта', max_length=30)
    message = models.TextField(verbose_name='Описание вопроса')
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Дата')

    def __str__(self):
        return 'Тема %s, категория: %s' % (self.topic, self.category)

    class Meta:
        db_table = "Feedbacks"
        ordering = ["-date"]
        verbose_name = "Обратная связь"
        verbose_name_plural = "Сообщения по обратной связи"

admin.site.register(Feedback)

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = 'Автор')
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolite_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Дата')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = 'Статья')
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий к статьям блога'
        ordering = ['-date']

admin.site.register(Comment)