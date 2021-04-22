from django.shortcuts import render
from products.models import Product


def index(request):
    """
    A view to return the index page
    """
    home_new_arrivals = Product.objects.filter(category__name='new_arrivals')

    context = {
        'home_new_arrivals': home_new_arrivals
    }

    return render(request, 'home/index.html', context)
