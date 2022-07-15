from django.shortcuts import render


def index(request):
    context = {
        'title': 'About Me'
    }
    return render(request, 'main/index.html', context)


def services(request):
    context = {
        'title': 'Services'
    }
    return render(request, 'main/services.html', context)


def skills(request):
    context = {
        'title': 'Skills'
    }
    return render(request, 'main/skills.html', context)


def portfolio(request):
    context = {
        'title': 'Portfolio'
    }
    return render(request, 'main/portfolio.html', context)


def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'main/contact.html', context)
