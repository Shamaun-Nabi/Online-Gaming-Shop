from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index,signup,loginPage,contactPage,storePage,productDetail,logout,userProfile

urlpatterns = [
    path('',index,name='index'),
    path('signup/',signup,name='signUp'),
    path('login/',loginPage,name='login'),
    path('contact/',contactPage,name='contact'),
    path('store/',storePage,name='store'),
    path('store/Product',productDetail,name='productDetails'),
    path('profile',userProfile,name="profile"),
    path('logout/',logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)