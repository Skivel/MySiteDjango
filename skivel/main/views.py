from django.shortcuts import render
from .models import Me, Skills, Portfolio, ContactMe


def index(request):
    my = Me.objects.all()
    context = {
        'title': 'About Me',
        'my': my
    }
    return render(request, 'main/index.html', context)


def services(request):
    context = {
        'title': 'Services'
    }
    return render(request, 'main/services.html', context)


def skills(request):
    my_skills = Skills.objects.order_by('-skills')
    context = {
        'title': 'Skills',
        'skills': my_skills
    }
    return render(request, 'main/skills.html', context)


def portfolio(request):
    context = {
        'title': 'Portfolio'
    }
    return render(request, 'main/portfolio.html', context)


def contact(request):
    my = Me.objects.all()
    user_contact = ContactMe.objects.all()
    context = {
        'title': 'Contact',
        'contact': user_contact,
        'my': my
    }
    return render(request, 'main/contact.html', context)
