"""
Products admin.py
"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Admin display for product
    """
    list_display = (
        'sku',
        'name',
        'price',
        'category',
        'image',
    )
    search_fields = ['name', 'category', 'sku']
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin display for category
    """
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ['name', 'friendly_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
