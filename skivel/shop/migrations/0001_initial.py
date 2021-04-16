# Generated by Django 3.2 on 2021-04-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]


operations = [
    migrations.CreateModel(
        name='Asort',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title', models.CharField(max_length=50, verbose_name='Назва')),
            ('price', models.CharField(max_length=10, verbose_name='Ціна')),
            ('characteristics', models.TextField(verbose_name='Характеристики')),
            ('date', models.DateField(verbose_name='Дата'))
        ],
    ),
]
