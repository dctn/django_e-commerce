from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def products(request):
    all_products = Products.objects.all()

    context = {
        "products":all_products
    }
    return render(request,"products.html",context)


def product_details(request,product_id):
    product = get_object_or_404(Products,id=product_id)

    context = {
        "product":product
    }
    return render(request,"product-details.html",context)