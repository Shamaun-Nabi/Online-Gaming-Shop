from django.db import models
from django.contrib.auth.models import User
from ourGames.models import Game

# Create your models here.

class ShopCart(models.Model):
    games=models.ForeignKey(Game,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.games.name

