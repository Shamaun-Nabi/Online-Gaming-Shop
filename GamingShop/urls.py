from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index,signup,contactPage,storePage,productDetail,logout,userProfile,cart,check_out,showProfile,OrderPage,loginPage

urlpatterns = [
    path('',index,name='index'),
    path('signup/',signup,name='signUp'),
    path('cart/',cart,name='cart'),
    path('check-out/',check_out,name='check-out'),
    path('login/',loginPage,name='login'),
    path('contact/',contactPage,name='contact'),
    path('store/',storePage,name='store'),
    path('store/Product',productDetail,name='productDetails'),
    path('profile',userProfile,name="profile"),
    path('showProfile/',showProfile,name="showProfile"),
    path('order/',OrderPage,name="order"),
    path('logout/',logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)