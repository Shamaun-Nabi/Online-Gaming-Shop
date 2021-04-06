from django.contrib import admin
from .models import Customer
from .models import Order

# Register your models here.

class OrderInfo(admin.ModelAdmin):
    list_display=['customer','product','price','quantity','phone']
    
class CustomerInfo(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','phone',]
    
admin.site.register(Customer,CustomerInfo)
admin.site.register(Order,OrderInfo)
