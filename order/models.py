from django.db import models
from artisan import models as artisan_models
from client import models as client_models
from product import models as product_models
# Create your models here.
STATUS_CHOICES = (
    ('PENDING', 'En attente'),
    ('PREPARING', 'En préparation'),
    ('SHIPPED', 'Expédié'),
    ('DELIVERED', 'Livré'),
    ('CANCELLED', 'Annulé'),
)
class Order(models.Model):
    artisan = models.ForeignKey(artisan_models.Artisan,on_delete=models.CASCADE,related_name="artisan_order")
    client = models.ForeignKey(client_models.Clinet, on_delete=models.CASCADE, related_name="client_order")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=120,choices=STATUS_CHOICES, null=True,blank=True,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, null=True,blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return  self.artisan.user.username 
    


    
