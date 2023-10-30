from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from women.models import User, Courses


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
    course_lst = {"course_lst": (course for course in Courses.objects.all()),
                 "title": "COURSES" }
    return render(request, 'women/courses.html', context=course_lst)

def course_by_slug(request, course_slug):
    course = {"course": Courses.objects.get(slug=course_slug),
              "title": get_object_or_404(Courses, slug=course_slug).name}
    return render(request, 'women/one_course.html', context=course)



def sign_in(request):
    data = {'title': 'Войдите'}
    return render(request, 'women/sign_in.html', context=data)




def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
