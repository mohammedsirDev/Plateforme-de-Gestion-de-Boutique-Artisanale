from django import forms
from artisan import models 
from order import models as order_models
class ArtisanSetupForm(forms.ModelForm):

    class Meta:
        model = models.Artisan
        fields = [
            'shop_name',
            'shop_description',
            'phone',
            'shop_image',
        ]

        widgets = {
            'shop_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your shop name'
            }),

            'shop_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your shop and products',
                'rows': 4
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),

            'shop_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = order_models.Order
        fields = ['status', 'first_name', 'last_name', 'adresse', 'phone']

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }