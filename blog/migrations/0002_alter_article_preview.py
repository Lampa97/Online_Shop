# Generated by Django 5.1.3 on 2024-12-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="preview",
            field=models.ImageField(
                blank=True, default="placeholder.png", null=True, upload_to="articles", verbose_name="Изображение"
            ),
        ),
    ]
