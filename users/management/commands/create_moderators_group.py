from django.core.management.base import BaseCommand

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = "Creates Moderators group"

    def handle(self, *args, **options):
        moderators_group = Group.objects.create(name='Модератор продуктов')
        unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_permission = Permission.objects.get(codename='delete_product')
        moderators_group.permissions.add(unpublish_permission, delete_permission)

        self.stdout.write(self.style.SUCCESS(f"Successfully created Group {moderators_group.name}"))
