# Generated by Django 5.1.3 on 2024-12-05 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите название категории', max_length=100, unique=True, verbose_name='Название'),
        ),
    ]
