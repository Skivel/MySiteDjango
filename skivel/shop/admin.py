from django.contrib import admin
from .models import Category, CPU, Smartphone, CartProduct, Cart, Customer

admin.site.register(Category)
admin.site.register(CPU)
admin.site.register(Smartphone)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)