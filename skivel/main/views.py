from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/html/index.html')


def info(request):
    return render(request, 'main/html/info.html')


def about(request):
    return render(request, 'main/html/about.html')