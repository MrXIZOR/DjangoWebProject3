"""
Definition of urls for DjangoWebProject3.
"""

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()


from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),
    path('link/', views.link, name='link'),
    path('blog/', views.blog, name='blog'),
    path('<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('favicon.ico/', RedirectView.as_view(url='/static/favicon.ico'), name='favicon'),
    path('videopost/', views.videopost, name='videopost'),
    path('feedback/', views.feedback, name='feedback'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

