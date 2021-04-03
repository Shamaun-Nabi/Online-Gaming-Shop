from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=500)
    re_password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='Product_img/images',default='default.png')
    
    @staticmethod
    def get_customer_by_mail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return False
        
    @staticmethod
    def customerInfo():
        return Customer.objects.all()
    
    def register(self):
        self.save()