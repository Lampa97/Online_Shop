# Generated by Django 5.1.3 on 2024-12-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_article_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="articles", verbose_name="Изображение"),
        ),
    ]
