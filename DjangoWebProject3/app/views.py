"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm
from .forms import FeedbackForm 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'AI Project | Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'AI Project | Контакты',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'AI Project | О нас',
            'message':'Сведение о нас',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'title':'AI Project | Регистрация',
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )
def link(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/link.html',
        {
            'title':'AI Project | Полезные ссылки',
            'year':datetime.now().year,
        }
    )
def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'AI Project | Блог',
            'posts':posts,
            'year':datetime.now().year,
        }
     )
def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()
            
    assert isinstance(request, HttpRequest)  
    return render(
        request,
        'app/blogpost.html',
        {
            'title':'AI Project | Блог',
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments,
            'form': form,
            'year':datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page"""

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()

            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
            'title':'AI Project | Добавление статьи',
            'blogform':blogform,
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'AI Project | Онлайн-курс',
            'year':datetime.now().year,
        }
    )

def feedback(request):
    assert isinstance(request, HttpRequest)
    data = None
    category = {'1': 'Ошибка', '2':'Блог',
                '3':'Авторские права'}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_f = form.save(commit=False)
            feedback_f.name = form.cleaned_data['name']
            feedback_f.topic = form.cleaned_data['topic']
            feedback_f.category = category[ form.cleaned_data['category'] ]
            feedback_f.answer = form.cleaned_data['answer']
            feedback_f.email = form.cleaned_data['email']
            feedback_f.message = form.cleaned_data['message']
            feedback_f.save()
            form = None
            #data = dict()
            #data['name'] = form.cleaned_data['name']
            #data['topic'] = form.cleaned_data['topic']
            #data['category'] = category[ form.cleaned_data['category'] ]
            #if(form.cleaned_data['answer'] == True):
            #    data['answer'] = 'Да'
            #else:
            #    data['answer'] = 'Нет'
            #data['email'] = form.cleaned_data['email']
            #data['message'] = form.cleaned_data['message']
            #form = None
    else:
        form = FeedbackForm()
    return render(
        request,
        'app/feedback.html',
        {
            'title':'AI Project | Обратная связь',
            'form': form,
            'data':data
        }
    )