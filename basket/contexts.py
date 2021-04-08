from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    if total > settings.DISCOUNT_THRESHOLD:
        promotion = total * Decimal(settings.STANDARD_PROMOTION_PERCENTAGE / 100)
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        promotion = 0
        discount_delta = settings.DISCOUNT_THRESHOLD

    grand_total = promotion + total

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
