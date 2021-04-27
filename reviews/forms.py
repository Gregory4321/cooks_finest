"""
Reviews forms.py
"""
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for product review
    """
    class Meta:
        model = Review
        exclude = ('user_profile', 'product',)

    review_rating = forms.IntegerField(
        label='Rating: 0 - 5',
        widget=forms.NumberInput(
            attrs={'min': 0, 'max': 5, 'class': 'text-center'})
    )
