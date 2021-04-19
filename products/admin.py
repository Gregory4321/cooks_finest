from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'category',
        'image',
    )
    search_fields = ['name', 'category', 'sku']
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ['name', 'friendly_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
