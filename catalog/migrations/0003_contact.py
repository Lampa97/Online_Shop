# Generated by Django 5.1.3 on 2024-12-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_category_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("individual_number", models.CharField(max_length=100, verbose_name="ИНН")),
                ("address", models.TextField(verbose_name="Адрес")),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ["country", "address"],
            },
        ),
    ]
