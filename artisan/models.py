from django.db import models
from userauths import models as userauths_model
# Create your models here.

class Artisan(models.Model):

    user = models.OneToOneField(userauths_model.User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=120, null=True,blank=True)
    shop_description = models.TextField()
    is_verified = models.BooleanField(default=False)
    shop_image = models.FileField(upload_to="images", max_length=100, null=True,blank=True)
    phone = models.CharField(max_length=120, null=True,blank=True)

    def __str__(self):
        return self.user.username 




