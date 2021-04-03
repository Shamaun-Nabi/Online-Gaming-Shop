from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerInfo(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','phone','password',]
    
admin.site.register(Customer,CustomerInfo)
