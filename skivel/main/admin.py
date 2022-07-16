from django.contrib import admin
from .models import *


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_editable = ['status']


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['language', 'skills']
    list_editable = ['skills']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'git_url']


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

