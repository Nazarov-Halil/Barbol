# forms.py
from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'quantity-input'}))
    product_id = forms.IntegerField(widget=forms.HiddenInput())
