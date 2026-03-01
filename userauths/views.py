from django.shortcuts import render
from userauths import forms as userauths_forms
from django.shortcuts import render,redirect
# Create your views here.
from client import models as client_modules
from django.contrib import messages
from artisan import models as artisan_models
from django.contrib.auth import authenticate, login, logout 
def register_view(request):
   
    if request.user.is_authenticated:
        return redirect("/")
    form = userauths_forms.UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password1 = form.cleaned_data.get("password1")
        email = form.cleaned_data.get("email")
        user_type = form.cleaned_data.get("user_types")
        if user_type == "Client":
            client_modules.Clinet.objects.create(user=user)
        else:
            artisan_models.Artisan.objects.create(user=user)

        user_ = authenticate(email=email,password=password1)
        login(request,user_)
        print(user_type)
        if user_type == "Client":

            return redirect("/") 
        else:
            return redirect("artisan:dashboard_artisan")
     
    
  
    else:
    
        form =userauths_forms.UserRegisterForm()

    return render(request,"userauths/register.html",{'form':form})





def login_view(request):
  if request.method == "POST":
      form = userauths_forms.LoginForm(request.POST)
      if form.is_valid():

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email,password=password)
        if user is not None:
            login(request, user)
            
            if client_modules.Clinet.objects.filter(user=user).exists():
                    return redirect("client:index")  # or "/"

                # ✅ Check if Artisan
            elif artisan_models.Artisan.objects.filter(user=user).exists():
                    return redirect("artisan:dashboard_artisan")

              
            
        else:
            messages.error(request,"This user not find")
            

        
    
      
  


  return render(request,"userauths/login_view.html")

from django.views.decorators.http import require_POST


def logout_view(request):
    logout(request)
    return redirect("/")