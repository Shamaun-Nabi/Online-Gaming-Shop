from django.db import models


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=500)
    re_password=models.CharField(max_length=500)
    
    @staticmethod
    def get_customer_by_mail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    
    
    def register(self):
        self.save()