from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from django.views import  View
from ourGames.models import Game
from Customer.models import Customer


class Cart(View):
    def get(self , request):
        ids = list(request.session.get('addCart').keys())
        products = Game.get_products_by_id(ids)
        return render(request , 'store.html' , {'products' : products} )