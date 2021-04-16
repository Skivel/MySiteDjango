from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Головна сторінка'
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Про нас'
    }
    return render(request, 'main/about.html', data)


def info(request):
    data = {
        'title': 'Інфо'
    }
    return render(request, 'main/info.html', data)