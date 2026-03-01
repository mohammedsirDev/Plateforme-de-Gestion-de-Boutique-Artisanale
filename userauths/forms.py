from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

USER_TYPE=(
    ("Artisan","Artisan"),
    ("Client","Client")
)
class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'John Doe'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'John Doe'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'worksire99@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'*********'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'********'}))
    user_types = forms.ChoiceField(choices=USER_TYPE,widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model= User
        fields = ['first_name','last_name', 'email','password1','password2',"user_types"]




    
 
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'worksir99@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'*********'}))
    class Meta:
        model = User
        fields =['email','password']