from django import forms

from order import models as order_models

class AddOrder(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aicha'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bennani'})
    )
    adresse = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '12 rue des Artisans'})
    )
    phone = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "pattern": "[0-9]{10}",
            "maxlength": "10",
            "inputmode": "numeric",
        })
    )

    class Meta:
        model = order_models.Order
        fields = ['first_name', 'last_name', 'adresse', 'phone']