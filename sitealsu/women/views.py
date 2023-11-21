from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from women.models import User, Category


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


def categories(request):
    categories_lst = {"categories_lst": (category for category in Category.objects.all()),
                 "title": "Categories" }
    return render(request, 'women/categories.html', context=categories_lst)


def category_by_slug(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    users = category.user_set.filter(cat=category)
    data = {
        "category": category,
        "title": category.name,
        "users": users,
    }
    return render(request, 'women/category.html', context=data)


def sign_in(request):
    data = {'title': 'Войдите'}
    return render(request, 'women/sign_in.html', context=data)




def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
