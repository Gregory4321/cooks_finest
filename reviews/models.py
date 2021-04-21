from django.db import models
from profiles.models import UserProfile


class Review(models.Model):
    product = models.ForeignKey(
        'products.Product', null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_review')
    created_on = models.DateTimeField(auto_now_add=True)
    review_title = models.CharField(max_length=254)
    review_content = models.TextField(
        max_length=1000, null=False, blank=False, default='')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.review_title
