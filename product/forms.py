from django import forms

from product.models import Products 
from category import models
class ProductFormAdd(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nom du produit'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Description du produit'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Prix du produit'}))
    stock = forms.IntegerField(
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Quantité en stock',
        'min': 1,  # prevent negative numbers
         # optional, to force using buttons
    })
)
    product_image = forms.ImageField(
    widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))
    category = forms.ModelChoiceField(
    queryset=models.Category.objects.all(),
    widget=forms.Select(attrs={
        'class': 'form-control'
    })
)

    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'stock', 'product_image','category']