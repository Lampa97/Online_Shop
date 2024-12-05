from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(name='Мебель', description='Крепкая древесина')

        products = [
            {'name': 'Шкаф', 'description': 'Для хранения вашей одежды', 'price': 2000.00, 'category': category},
             {'name': 'Ящик', 'description': 'Для хранения ваших инструментов', 'price': 899.99, 'category': category},
              {'name': 'Полка', 'description': 'Если не хватило места для одежды или инструментов', 'price': 599.99, 'category': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))