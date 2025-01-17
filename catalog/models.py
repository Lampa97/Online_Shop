from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название категории", unique=True
    )
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название продукта")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="products", verbose_name="Владелец", null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Contact(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")
    individual_number = models.CharField(max_length=100, verbose_name="ИНН")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return f"{self.country} {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["country", "address"]
