from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def signup(request):
    return render(request,'signup.html')

def loginPage(request):
    return render(request,'login.html')

def contactPage(request):
    return render(request,'contact.html')

def storePage(request):
    return render(request,'store.html')


def productDetail(request):
    return render(request,'product_view.html')
