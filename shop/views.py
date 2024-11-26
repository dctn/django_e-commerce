from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    cart_items = Cart.objects.filter(user=request.user)

    total_item = 0
    for product in cart_items:
        total_item += product.quantity

    return render(request,"index.html",{"total_item":total_item})

def products(request):
    cart_items = Cart.objects.filter(user=request.user)

    total_item = 0
    for product in cart_items:
        total_item += product.quantity
    all_products = Products.objects.all()

    context = {
        "products":all_products,
        "total_item":total_item
    }
    return render(request,"products.html",context)


def product_details(request,product_id):
    cart_items = Cart.objects.filter(user=request.user)

    total_item = 0
    for product in cart_items:
        total_item += product.quantity
    all_products = Products.objects.all()
    
    product = get_object_or_404(Products,id=product_id)

    context = {
        "product":product,
        "total_item":total_item
    }
    return render(request,"product-details.html",context)


@login_required
def add_to_cart(request,product_id):
     product = get_object_or_404(Products,id=product_id)

     cart = Cart.objects.filter(user=request.user,product=product)
     if cart:
         cart = Cart.objects.get(user=request.user,product=product)
         cart.quantity += 1  
         cart.save()    
     else:
         Cart.objects.create(user=request.user,product=product,quantity=1)

     return redirect("products")