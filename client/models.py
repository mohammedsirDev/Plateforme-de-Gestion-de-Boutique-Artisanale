from django.db import models

from userauths import models as userauths_models
# Create your models here.

class Clinet(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete=models.CASCADE, related_name="client")

    def __str__(self):
        return self.user.first_name
    

