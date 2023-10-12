from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.
def index(request):
    if request.GET:
        return HttpResponse('|'.join([f"{key}={value}" for key, value in request.GET.items()]))
    return HttpResponse(reverse('edit_page', args=['slug']))


def archive(request, year):
    return HttpResponse(f"{year}")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def update_page(request, slug):
    return HttpResponse(f"{slug}")

