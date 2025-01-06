# Generated by Django 5.1.3 on 2024-12-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, default="placeholder.png", null=True, upload_to="products", verbose_name="Изображение"
            ),
        ),
    ]
