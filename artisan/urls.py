from django.urls import path
from artisan import views

app_name="artisan"

urlpatterns = [
  
    path("dashboard_artisan/",views.dashboard_artisan, name="dashboard_artisan"),
    path("add_product/",views.add_product, name="add_product"),
    path("delete-product/<int:id>/", views.delete_product, name="delete_product"),
    path("edit-product/<int:id>/", views.edit_product, name="edit_product"),
    path("setup_artisan/", views.setup_artisan, name="setup_artisan"),
    path("orders/", views.my_orders, name="orders"),
    path("update_order/<int:pk>/", views.update_order, name="update_order"),
    path("export-orders/", views.export_orders, name="export_orders"),

    
    
]

