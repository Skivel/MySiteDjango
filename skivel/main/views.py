from django.shortcuts import render
from django.http import HttpResponse


def index():
    pass


def about(request):
    return HttpResponse("<h1>About Page</h1>")
