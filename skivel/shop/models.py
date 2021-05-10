from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва категорії')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Test', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Назва товару')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Опис', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупець', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey('Product', verbose_name='Товар', on_delete=models.CASCADE)
    unmount = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Загальна Ціна')

    def __str__(self):
        return "Продукт: {} (корзина)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Власник', on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Загальна Ціна')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефону')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупець: {} {}".format(self.user, self.first_name, self.user.last_name)


class Specification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name='Назва товару для характеристик')

    def __str__(self):
        return "Характеристики для товару: {}".format(self.name)
