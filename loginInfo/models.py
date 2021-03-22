from django.db import models


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mail=models.EmailField()
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=500)
    re_password=models.CharField(max_length=500)
    
    
    def register(self):
        self.save()