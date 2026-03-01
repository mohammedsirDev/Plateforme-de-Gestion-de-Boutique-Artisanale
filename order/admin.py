from django.contrib import admin
from order import models
# Register your models here.
class OrderClient(admin.ModelAdmin):
    list_display =['artisan','client','status','adresse','phone']
    
admin.site.register(models.Order,OrderClient)