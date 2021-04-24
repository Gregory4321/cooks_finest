"""
Checkout app.py
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout app config
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
