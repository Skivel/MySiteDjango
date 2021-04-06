from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render()


def about(request):
    return HttpResponse("<h1>About Page</h1> <p>Created by: Denis Buhrov</p>")