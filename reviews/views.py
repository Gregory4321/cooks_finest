from django.shortcuts import render
from .forms import ReviewForm


def add_review(request):
    """
    Add a review to a product
    """

    form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
