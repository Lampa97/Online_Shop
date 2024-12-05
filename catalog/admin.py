from django.contrib import admin
from .models import Category, Product, Contact

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'individual_number', 'address')
    search_fields = ('country', 'individual_number', 'address')
    list_filter = ('country', 'individual_number', 'address')