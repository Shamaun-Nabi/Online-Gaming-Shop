from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=10)
    id = models.IntegerField(primary_key=True)

class Games(models.Model):
    title = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    platform = models.CharField(max_length=10)
    categories = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)


