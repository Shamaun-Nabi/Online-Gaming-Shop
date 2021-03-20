from django.db import models

# Create your models here.

class Accessories(models.Model):
    name = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=True)