from django.db import models
from Cart.models import Cart

# Create your models here.

class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=10)
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
