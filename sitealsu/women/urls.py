from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('news', views.news, name='news'),
    path('about_me', views.about_me, name='about_me'),
    path('courses', views.courses, name='courses'),
]


