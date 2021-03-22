from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from loginInfo.models import Customer

# Create your views here.
def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=="GET":
        return render(request,'signup.html')
    else:
        postData=request.POST
        first_name=postData.get('first_name')
        last_name=postData.get('last_name')
        email=postData.get('email')
        phone=postData.get('phone')
        password=postData.get('password')
        re_password=postData.get('re_password')
        all_values={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'phone':phone,
        }
        # Validation
        error_msg=None
        if password!=re_password:
            error_msg="Hey! Your Password Not Matched"
        elif len(phone)<11:
            error_msg="Hey Your Phone number must be 11 digit"
        
        if not error_msg:
            customer_Details=Customer(first_name=first_name,last_name=last_name,mail=email,phone=phone,password=password,re_password=re_password)
            customer_Details.register()
            return redirect('index')
        else:
            data={
                "error":error_msg,
                "info":all_values
            }
            return render(request,'signup.html',data)
    # return render(request,'signup.html')

def loginPage(request):
    return render(request,'login.html')

def contactPage(request):
    return render(request,'contact.html')

def storePage(request):
    return render(request,'store.html')


def productDetail(request):
    return render(request,'product_view.html')
