from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from loginInfo.models import Customer,Order
from ourGames.models import Game,Category
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View

# Create your views here.
def index(request):
    currentUser=request.session.get('customer_fname')
    print("Hello Mr",currentUser)
    
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
        password=postData.get('password')
        re_password=postData.get('re_password')
        image=request.FILES.get('image')
        # print(image)
        all_values={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
        }
        # Validation
        
        error_msg=None
        customer_Details=Customer(first_name=first_name,last_name=last_name,email=email,password=password,re_password=re_password,image=image)
        if password!=re_password:
            error_msg="Hey! Your Password Not Matched"
        elif Customer.objects.filter(email=email).exists():
            error_msg="This Email Has Been Already Registered"
        
        elif len(password)<8:
            error_msg="Password must Be 8 character"
      
        if not error_msg:
            customer_Details.password=make_password(customer_Details.password)
            # a = User.objects.create_user(username=first_name,first_name=first_name,last_name=last_name, email=email,password=password)
            # a.save()
            customer_Details.register()
        
            return redirect('login')
        else:
            data={
                "error":error_msg,
                "info":all_values
            }
            return render(request,'signup.html',data)
    return render(request,'signup.html')

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
                print(request.session['customer_id'])
                request.session['customer_fname']=loginCustomer.first_name
                request.session['customer_lname']=loginCustomer.last_name
                request.session['email']=loginCustomer.email
                # print(request.session['email'])
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
    cart_add = request.session.get('cart_add')
    if not cart_add:
        request.session['cart_add'] = {}
    # request.session.flush()
    data="1"
    postdata=request.GET
    product= Game.getAllProducts()
    category=Category.category()
    categoryId=postdata.get('category')
    cart=request.POST.get('addCart')
    remove = request.POST.get('remove')
    cart_add=request.session.get('cart_add')
    print(cart_add)
    if cart:
        if cart_add:
            quantity=cart_add.get(cart)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_add.pop(cart)
                    else:
                        cart_add[cart]=quantity-1  
                else:   
                    cart_add[cart]=quantity+1
            else:
                cart_add[cart]=1
                print(cart_add[cart])
        else:
            cart_add={}
            cart_add[cart]=1
        request.session['cart_add']=cart_add
        print(request.session ['cart_add'],cart)
    # cart_add=request.session['cart_add']
    # if cart_add:
    #     quantity=cart_add.get(cart)
    #     if quantity:
    #         if remove:
    #             if quantity<=1:
    #                 cart_add.pop(cart)
    #             else:
    #              cart_add[cart]=quantity-1  
    #         else:   
    #             cart_add[cart]=quantity+1
    #     else:
    #         cart_add[cart]=1
    #         print(cart_add[cart])
    # else:
    #     cart_add={}
    #     cart_add[cart]=1
    # request.session['cart_add']=cart_add
    # print(request.session ['cart_add'],cart)
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


def showProfile(request):
    loginCustomer_fname=request.session.get('customer_fname')
    loginCustomer_lname=request.session.get('customer_lname')
    loginCustomer_email=request.session.get('email')

    loginCustomer=Customer.get_customer_by_mail(loginCustomer_email)
    pic=loginCustomer.image
    
    customerInfo={
        'fname':loginCustomer_fname,
        'lname':loginCustomer_lname,
        'email':loginCustomer_email,
        'pic':pic
    }
    

    
    print(loginCustomer)
    # update=Customer()
    # update_details=Customer(first_name=update_fname,last_name=update_lname,email=update_email)
    
    
    return render(request,"showProfile.html",customerInfo)

def userProfile(request):
    loginCustomer_fname=request.session.get('customer_fname')
    loginCustomer_lname=request.session.get('customer_lname')
    loginCustomer_email=request.session.get('email')
    loginCustomer=Customer.get_customer_by_mail(loginCustomer_email)
    print(loginCustomer)
    pic=loginCustomer.image
    customerInfo={
        'fname':loginCustomer_fname,
        'lname':loginCustomer_lname,
        'email':loginCustomer_email,
        'pic':pic
    }
        # Update Info:
    # update_fname=request.POST.get('fname')
    # update_lname=request.POST.get('lname')
    # update_email=request.POST.get('email')
    # loginCustomer.first_name=update_fname
    # loginCustomer.last_name=update_lname
    # loginCustomer.email=update_email
    # loginCustomer.save()
    # request.session['customer_fname']=loginCustomer.first_name
    # request.session['customer_lname']=loginCustomer.last_name
    # request.session['email']=loginCustomer.email
    print(customerInfo)
    

    

    return render(request,'profile.html',customerInfo)




def cart(request):
    ids=list(request.session.get('cart_add').keys())
    print(ids)
    # ids=[int(i) for i in ids]
    games=Game.get_products_by_id(ids)
    return render(request,'cart.html',{'games':games})


def check_out(request):
    customer=request.session.get("customer_id")
    address=request.POST.get('address')
    phone=request.POST.get('Phone')
    cart=request.session.get("cart_add")
    products=Game.get_products_by_id(list(cart.keys()))
    # address=request.POST.get('address')
    print("User_name is",customer,address,phone,cart,products)
    for product in products:
        order=Order(customer=Customer(id=customer),
                    product=product,
                    price=product.price,
                    address=address,
                    phone=phone,
                    quantity=cart.get(str(product.id))
                    )
        order.placeOrder()
    request.session['cart_add']={}
    return redirect('cart')

def OrderPage(request):
    customer=request.session.get('customer_id')
    orders=Order.getCustomerByID(customer)
    print(customer,orders)
    return render(request,'order.html',{'orders':orders})


def logout(request):
    request.session.clear()
    return redirect('login')
