from django.db import models
from artisan import models as artisan_module
from category import models as models_category
# Create your models here.
class Products(models.Model):
    artisan = models.ForeignKey(artisan_module.Artisan, on_delete=models.CASCADE,null=True,blank=True, related_name="products_artisan")
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    stock  = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    product_image = models.FileField(upload_to="images",null=True,blank=True)
    category = models.ForeignKey(
        models_category.Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    def __str__(self):
        return self.artisan.user.username
    

