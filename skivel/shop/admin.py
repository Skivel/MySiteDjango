from django import forms
from django.contrib import admin
from .models import Category, CPU, Smartphone, CartProduct, Cart, Customer


class CpuCategoryChoiceField(forms.ModelChoiceField):
    pass


class CpuAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return CpuCategoryChoiceField(Category.objects.filter(slug='cpu'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneCategoryChoiceField(forms.ModelChoiceField):
    pass


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return SmartphoneCategoryChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CPU, CpuAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
