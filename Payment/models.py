from django.db import models

# Create your models here.

class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=10)

