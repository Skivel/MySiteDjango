from PIL import Image

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class MinResolutionMirrorException(Exception):
    pass


class MaxResolutionMirrorException(Exception):
    pass


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:
    objects = LatestProductsManager()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва категорії')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (1000, 1000)
    MAX_IMG_SIZE = 3145728

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

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_width, min_height = self.MIN_RESOLUTION
        max_width, max_height = self.MAX_RESOLUTION
        if img.width < min_width or img.height < min_height:
            raise MinResolutionMirrorException('Розширення зображення менше мінімального!')
        if img.width > max_width or img.height > max_height:
            raise MaxResolutionMirrorException('Розширення зображення більше максимального!')


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
