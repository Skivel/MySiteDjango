from django.db import models


class Me(models.Model):
    title = models.CharField(verbose_name='Заговолок', max_length=255)
    description = models.TextField(verbose_name='Анотація')
    img = models.ImageField()

    class Meta:
        verbose_name = 'Me'
        verbose_name_plural = 'Me'


class Services(models.Model):
    pass


class Skills(models.Model):
    pass


class Portfolio(models.Model):
    pass


class Contact(models.Model):
    pass
