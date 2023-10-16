from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


# Create your views here.
def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'women/index.html', context=data)

def sign_up(request):
    data = {'title': 'Регистрация'}
    return render(request, 'women/sign_up.html', context=data)


def news(request):
    data = {'title': 'Новости'}
    return render(request, 'women/news.html', context=data)

def about_me(request):
    data = {'title': 'Обо мне'}
    return render(request, 'women/about_me.html', context=data)

def courses(request):
    data = {'title': 'Курсы'}
    return render(request, 'women/courses.html', context=data)


def sign_in(request):
    data = {'title': 'Войдите'}
    return render(request, 'women/sign_in.html', context=data)




def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
