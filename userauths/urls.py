from django.urls import path

from userauths import views
app_name ="userauths"
urlpatterns = [
    path("register/",views.register_view, name="register"),
    path("logout_view/", views.logout_view, name="logout_view"),
    path("login_view/", views.login_view, name="login_view"),
  
   
]
