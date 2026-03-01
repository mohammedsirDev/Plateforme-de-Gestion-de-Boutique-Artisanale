from django.urls import path
from client import views

app_name="client"

urlpatterns = [
  
    path("",views.index, name="index"),
    path("product/<int:id>/", views.product_detail, name="product_detail"),
    path("checkout/<int:id>/", views.checkout, name="checkout"),
    path("client/search_result/", views.search, name="search"),
    path("client/commande_confirm/", views.commande_confirm, name="commande_confirm"),
    path("client/Page_des_commandes_clients/", views.Page_des_commandes_clients, name="Page_des_commandes_clients"),
    



  
 
    
]