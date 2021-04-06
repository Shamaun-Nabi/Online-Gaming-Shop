# from django.db import models
# from ourGames.models import Game
# from loginInfo.models import Customer
# import datetime

# # Create your models here.
# class Order(models.Model):
#     product=models.ForeignKey(Game,on_delete=models.CASCADE)
#     customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)
#     price=models.IntegerField()
#     date=models.DateField(default=datetime.datetime.today)
