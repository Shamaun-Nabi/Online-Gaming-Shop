from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=15)
    price=models.FloatField(default=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    
    
    def __str__(self):
        return self.name