from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        models = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price'
        ]
