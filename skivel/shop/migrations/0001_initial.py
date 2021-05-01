# Generated by Django 3.2 on 2021-05-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Сargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('characteristics', models.TextField(verbose_name='Характеристики')),
                ('price', models.CharField(max_length=10, verbose_name='Ціна')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': ('Товари',),
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
