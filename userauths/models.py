from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_TYPE=(
    ("Artisan", "Artisan"),
    ("Client", "Client")
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username =  models.CharField(max_length=120, null=True,blank=True)
    role = models.CharField(max_length=120, null=True,blank=True, default=True)
    user_image = models.FileField(upload_to="images", null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username or "User"
    
    def save(self,*args,**kwargs):
        email_username, _ = self.email.split("@")
        if self.username == "" or self.username == None:
            self.username = email_username

        super(User,self).save(*args,**kwargs)