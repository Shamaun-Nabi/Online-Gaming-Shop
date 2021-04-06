from django.db import models
from django.contrib.auth.models import User
from ourGames.models import Game
import datetime

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    re_password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='Product_img/images',default='default.png')
    phone=models.CharField(max_length=14,default='')
# Create your models here.
    
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

class Order(models.Model):
    product=models.ForeignKey(Game,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    phone=models.CharField(max_length=14,default="")
    address=models.TextField(default='')
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def getCustomerByID(customerId):
        return Order.objects.filter(customer=customerId)