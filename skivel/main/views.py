from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'templates/index.html')


def about(request):
    return HttpResponse("<h1>About Page</h1> <pCreated by: Denis Buhrov</p>")