from django.db import models
from Cart.models import Cart

# Create your models here.

class Customer(models.Model):
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=10)
    address_1 = models.TextField()
    address_2 = models.TextField()
    password = models.TextField()
    mail = models.EmailField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    order_id = models.ForeignKey(Cart, null=True, on_delete=models.SET_NULL)