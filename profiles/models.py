"""
Profile models.py
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    contact information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, default='', blank=True)
    default_phone_number = models.CharField(
        max_length=20,
        default='',
        blank=True)
    default_street_address1 = models.CharField(
        max_length=80,
        default='',
        blank=True)
    default_street_address2 = models.CharField(
        max_length=80,
        default='',
        blank=True)
    default_town_or_city = models.CharField(
        max_length=40,
        default='',
        blank=True)
    default_county = models.CharField(max_length=80, default='', blank=True)
    default_postcode = models.CharField(max_length=20, default='', blank=True)
    default_country = CountryField(
        blank_label='Select Country',
        null=True,
        blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the User Profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing Users: Save their profile
    instance.userprofile.save()
