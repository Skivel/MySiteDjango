from django.shortcuts import render, redirect
from .models import Me, Skills, Portfolio, ContactMe
from .forms import PostContact


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
    my_portfolio = Portfolio.objects.order_by('-id')
    context = {
        'title': 'Portfolio',
        'portfolio': my_portfolio
    }
    return render(request, 'main/portfolio.html', context)


def contact(request):
    my = Me.objects.all()
    user_contact = ContactMe.objects.all()
    initial_data = {
        'Name': 'name',
        'Email': 'email',
        'Massage': '1'
    }
    if request.method == 'POST':
        form = PostContact(request.POST, initial=initial_data)
        form.save()
        return redirect('/')
    else:
        form = PostContact
    context = {
        'title': 'Contact',
        'contact': user_contact,
        'my': my,
        'form': form
    }
    return render(request, 'main/contact.html', context)
