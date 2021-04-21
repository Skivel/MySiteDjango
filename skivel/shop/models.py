from django.db import models


class Сargo(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    characteristics = models.TextField('Характеристики')
    price = models.CharField('Ціна', max_length=10)
    date = models.DateField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товари',
        verbose_name_plural = 'Товари'