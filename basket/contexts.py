"""
Basket contexts.py
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """
    Contexts for basket contents
    """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Discount logic
    if total > settings.DISCOUNT_THRESHOLD:
        promotion = (
            total * Decimal(settings.STANDARD_PROMOTION_PERCENTAGE / 100))
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        promotion = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total

    grand_total = total - promotion

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'promotion': promotion,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
