"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog
from .models import Feedback


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Комментарий'}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'posted', 'author', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Содержание", 'posted': "Дата",'author':"Автор",'image':"Картинка"}

class FeedbackForm(forms.ModelForm):
    #name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    #topic = forms.CharField(label='Тема сообщения', min_length=2, max_length=100)
    #category = forms.ChoiceField(label='Категория вопроса',
    #                             choices=(('1','Ошибка'),
    #                                      ('2', 'Блог'),
    #                                      ('3', 'Авторские права')), initial=1)
    #answer = forms.BooleanField(label='Получить ответ?',
    #                            required=False)
    #email = forms.EmailField(label='Ваш e-mail', min_length=7)
    #message = forms.CharField(label='Описание вопроса',
    #                          widget=forms.Textarea(attrs={'rows':12,'cols':200}))
    class Meta:
        model = Feedback
        fields = ('name', 'topic', 'category', 'answer', 'email', 'message')
        labels = {'name':"Ваше имя", 'topic':"Тема сообщения", 'category':"Категория вопроса", 'answer':"Получить ответ?", 'email':"Ваш e-mail", 'message':"Описание вопроса"}

