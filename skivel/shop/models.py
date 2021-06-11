from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва категорії')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Назва категорії', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Назва товару')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Опис', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return self.title


class CPU(Product):
    core = models.CharField(max_length=2, verbose_name='Кількість ядер')
    threads = models.CharField(max_length=3, verbose_name='Кількість потоків')
    cesh = models.CharField(max_length=2, verbose_name='Кеш')
    power = models.CharField(max_length=3, verbose_name='ТДП')
    core_freq = models.CharField(max_length=5, verbose_name='Частота процессора')
    boost = models.BooleanField(default=True, verbose_name='Turbo Boost(+/-)')
    video = models.BooleanField(default=True, verbose_name='Встроєне графічне ядро(+/-)')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Діагональ екрану')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплею')
    reslution = models.CharField(max_length=255, verbose_name='Розширення екрану')
    accum_volume = models.CharField(max_length=200, verbose_name='Об\'єм акумулятора')
    ram = models.CharField(max_length=255, verbose_name='Оперативна пам\'ять')
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name='Максимальний об\'єм SD-карти')
    main_cam_mp = models.CharField(max_length=255, verbose_name='Основна камера')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальна камера')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупець', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
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
