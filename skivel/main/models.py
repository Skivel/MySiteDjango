from django.db import models


class Me(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Заговолок', max_length=255)
    description = models.TextField(verbose_name='Анотація')
    img = models.ImageField(verbose_name='Зображення', upload_to="static/me/img")
    age = models.IntegerField(verbose_name='Вік')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Номер телефону', max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    status = models.BooleanField(verbose_name='Статус зайнятості')

    class Meta:
        verbose_name = 'Me'
        verbose_name_plural = 'Me'


class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(verbose_name='Назва технології', max_length=144)
    skills = models.IntegerField(verbose_name='Розуміння %')

    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Назва проекту', max_length=255)
    description = models.TextField(verbose_name='Опис проекту')
    img = models.ImageField(verbose_name='Зображення', upload_to="static/portfolio/img")
    git_url = models.URLField(verbose_name='GitHub URL')



    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


class ContactMe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="'Ім'я", max_length=255)
    email = models.EmailField(verbose_name='Email')
    massage = models.TextField(verbose_name='Повідомлення')

    class Meta:
        verbose_name = 'Massage'
        verbose_name_plural = 'Massage'
