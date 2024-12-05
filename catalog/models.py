from django.db import models
from mypy.main import maybe_write_junit_xml


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание')

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/media', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
