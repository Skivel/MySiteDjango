from django.db import models


class Asort(models.Model):
    title = models.CharField('shop_asort', max_length=50),
    price = models.CharField('Ціна', max_length=10),
    characteristics = models.TextField('Характеристики'),
    date = models.DateField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Асортиметн/Каталог'
        verbose_name_plural = 'Асортиметн/Каталог'