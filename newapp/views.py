from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from newapp.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, BooleanField
from .models import Product ,CartItem
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
#def index(request):
 #   return HttpResponse(" Hello... This is my new project and you are under the application")

def index(request):
    return render(request, "index.html")

def registration(request):
    #import pdb;pdb.set_trace()
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        gender = request.POST['gender']
        
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if password != confirm_password:
            passnotmatch = True
            return render(request, "registration.html", {'passnotmatch':passnotmatch})
    

        user = User.objects.create_user(first_name=first_name,last_name=last_name,email= email, mobile_no=mobile_no,gender=gender,password=password )
        user.save()
        alert = True
        print("Your Registration is succsesfull")
        return render(request, "registration.html", {'alert':alert})
    return render(request, "registration.html")

def customer_login(request):
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email= email, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return HttpResponse("You are not a registered customer!!")
            else:
                return render(request, "profile.html")
        else:
            alert = True
            return render(request, "customer_login.html", {'alert':alert})
    return render(request, "customer_login.html")

@login_required(login_url = '/newapp/customer_login')
def profile(request):
      if request.method == "POST":
          image = request.FILES['image']

          profile = User.objects.create_user(image= image) 
          profile.save()
          alert = True
          
      return render(request, "profile.html")
      
def create_product(request):
    #import pdb;pdb.set_trace()
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']

    def __str__(self):
        return self.name 

def product_list(request):
    products = Product.objects.values('id', 'name', 'price')
    return render(request, 'product_list.html', {'products': products})

@login_required(login_url = '/newapp/customer_login')
def product_details(request, pk):
    prod_detail = Product.objects.get(id=pk)
    return render(request, 'product_details.html', {'prod_detail': prod_detail})

@login_required(login_url = '/newapp/customer_login')
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
    print(cart_items)

@login_required
def update_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)

    if request.POST.get('action') == 'increase':
        cart_item.quantity += 1
    elif request.POST.get('action') == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    
    cart_item.save()
    return redirect('newapp:view_cart')
 
    
@login_required(login_url = '/newapp/customer_login') 
def add_to_cart(request, pk):
    product_cart = get_object_or_404(Product, id=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product_cart, user=request.user)

    if not created:  # If the item already exists, increase the quantity
        cart_item.quantity += 1
    cart_item.save()

    messages.success(request, "Item added to cart successfully.")
    return redirect('newapp:view_cart')

"""
def add_to_cart(request, pk):
    product_cart = Product.objects.get(id=pk)
    cart_item, created  = CartItem.objects.get_or_create(product=product_cart, user=request.user)
    if created:                                               
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Item added to cart successfully.")
    return redirect('newapp:view_cart')
"""

@login_required(login_url = '/newapp/customer_login') 
def remove_from_cart(request, pk):
     cart_item = CartItem.objects.get(id=pk)
     cart_item.delete()
     return redirect('cart:view_cart')

def search(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = None
    print(results)
    return render(request, 'search.html', {'results': results})

@login_required(login_url='/newapp/customer_login')
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        if 'image' in request.FILES:
            user.image = request.FILES['image']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.mobile_no = mobile_no
        user.gender = gender
        user.address = address
        
        user.save()

        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('newapp:profile')

    context = {
        'user': user,
    }

    return render(request, 'edit_profile.html', context)

def Logout(request):
    logout(request)
    return redirect ("/")