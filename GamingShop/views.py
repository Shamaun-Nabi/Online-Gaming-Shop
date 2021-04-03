from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from loginInfo.models import Customer
from ourGames.models import Game,Category
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.views import View

# Create your views here.
def index(request):
    currentUser=request.user
    
    # print("You are "+request.session.get('email'))
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
        customer_Details=Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password,re_password=re_password)
        if password!=re_password:
            error_msg="Hey! Your Password Not Matched"
        elif len(phone)<11:
            error_msg="Hey Your Phone number must be 11 digit"
        elif Customer.objects.filter(email=email).exists():
            error_msg="This Email Has Been Already Registered"
        
        elif len(password)<8:
            error_msg="Password must Be 8 character"
      
        if not error_msg:
            customer_Details.password=make_password(customer_Details.password)
            a = User.objects.create_user(username=first_name,first_name=first_name,last_name=last_name, email=email,password=password)
            a.save()
            customer_Details.register()
            return redirect('login')
        else:
            data={
                "error":error_msg,
                "info":all_values
            }
            return render(request,'signup.html',data)
    # return render(request,'signup.html')

class LoginPage(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        postData=request.POST
        email=postData.get('email')
        password=postData.get('password')
        loginCustomer=Customer.get_customer_by_mail(email)
       
        error_msg=None
        if loginCustomer:
            flag=check_password(password,loginCustomer.password)
            if flag:
                request.session['customer_id']=loginCustomer.id
                a=request.session['customer_name']=loginCustomer.first_name
                print(a)
                request.session['email']=loginCustomer.email
                return redirect('index')
            else:
                error_msg="Email or Password Incorrect"
            
        else:
            error_msg="Email or Password Incorrect"
            print(email,password,loginCustomer)
            return render(request,'login.html',{'error':error_msg})


# def loginPage(request):
#     if request.method=="GET":
        # return render(request,'login.html')
    # else:
    #     postData=request.POST
    #     email=postData.get('email')
    #     password=postData.get('password')
    #     loginCustomer=Customer.get_customer_by_mail(email)
       
      
    #     error_msg=None
    #     if loginCustomer:
    #         flag=check_password(password,loginCustomer.password)
    #         if flag:
    #             request.session['customer_id']=loginCustomer.id
    #             a=request.session['customer_name']=loginCustomer.first_name
    #             print(a)
    #             request.session['email']=loginCustomer.email
    #             return redirect('index')
    #         else:
    #             error_msg="Email or Password Incorrect"
            
    #     else:
    #         error_msg="Email or Password Incorrect"
    #     print(email,password,loginCustomer)
        
    
    # return render(request,'login.html',{'error':error_msg})

def contactPage(request):
    return render(request,'contact.html')

def storePage(request):
    postdata=request.GET
    product= Game.getAllProducts()
    category=Category.category()
    categoryId=postdata.get('category')
    cart=request.POST.get('addCart')
    cart_add=request.session.get('cart_add')
    if cart_add:
        quantity=cart_add.get(cart)
        if quantity:
            cart_add[cart]=quantity+1
        else:
            cart_add[cart]=1
    else:
        cart_add={}
        cart_add[cart]=1
    request.session['cart_add']=cart_add
    print(request.session['cart_add'])
    if categoryId:
        product= Game.get_product_by_id(categoryId)
    else:
        product= Game.getAllProducts()
    all_data={}
    all_data['allProducts']=product
    all_data['category']=category
    return render(request,'store.html',all_data)


def productDetail(request):
    return render(request,'product_view.html')

def userProfile(request):
    customerInfo=Customer.customerInfo()
 
    print(customerInfo)
    return render(request,'profile.html',{'customer':customerInfo})

def logout(request):
    request.session.clear()
    return redirect('login')
