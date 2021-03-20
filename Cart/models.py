from django.db import models

# Create your models here.

class Cart(models.Model):
    item_id = models.IntegerField()
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    item_quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
