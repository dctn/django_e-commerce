from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
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

@login_required
def product_details(request,product_id):
    cart_items = Cart.objects.filter(user=request.user)

    total_item = 0
    for product in cart_items:
        total_item += product.quantity


    product = get_object_or_404(Products,id=product_id)
    cart = Cart.objects.filter(user=request.user,product=product)

    if request.method == "POST":
        form = AtcForm(request.POST)
        if form.is_valid():
             color_in_form = form.cleaned_data["color"]
             size_in_form = form.cleaned_data["size"]
             print(color_in_form)
             print(size_in_form)
             print("---------")
             if cart:
               
                already_cart = cart.filter(color=color_in_form,Size=size_in_form).first()
                # cart = Cart.objects.get(user=request.user,product=product)
                # color = cart.color
                # size = cart.Size

                if already_cart:
                    already_cart.quantity += 1  
                    already_cart.save()    
                else:
                    color = form.cleaned_data["color"]
                    size = form.cleaned_data["size"]
                    Cart.objects.create(user=request.user,product=product,quantity=1,color=color,Size=size)
                return redirect("products")
             else:
                color = form.cleaned_data["color"]
                size = form.cleaned_data["size"]
                Cart.objects.create(user=request.user,product=product,quantity=1,color=color,Size=size)
                return redirect("products")


    else:
         form =  AtcForm()
    product = get_object_or_404(Products,id=product_id)

    context = {
        "product":product,
        "total_item":total_item,
        "form":form
    }
    return render(request,"product-details.html",context)




def cart_summary(request):
    cart_items = Cart.objects.filter(user=request.user)

    context = {
        "cart_items":cart_items
    }

    return render(request,"cart_summary.html",context)