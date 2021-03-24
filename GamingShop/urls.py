from django.contrib import admin
from django.urls import path
from .views import index,signup,loginPage,contactPage,storePage,productDetail,logout

urlpatterns = [
    path('',index,name='index'),
    path('signup/',signup,name='signUp'),
    path('login/',loginPage,name='login'),
    path('contact/',contactPage,name='contact'),
    path('store/',storePage,name='store'),
    path('store/Product',productDetail,name='productDetails'),
    path('logout/',logout,name='logout'),
]