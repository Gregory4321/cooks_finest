"""
Product models.py
"""
from django.db import models
from django.db.models import Avg


class Category(models.Model):
    """
    Category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Return friendly name
        """
        return self.friendly_name


class Product(models.Model):
    """
    Products Form Fields
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, default='', blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image_url = models.URLField(max_length=1024, default='', blank=True)
    image = models.ImageField(default='', blank=True)

    def calculate_rating(self):
        """
        Calculate rating from reviews
        """
        self.rating = self.reviews.aggregate(Avg("review_rating"))[
            'review_rating__avg']
        self.save()

    def __str__(self):
        return self.name
