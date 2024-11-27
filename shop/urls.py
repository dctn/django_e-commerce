from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("products",views.products,name="products"),
    path("product_detail/<product_id>",views.product_details,name="product_details"),
    path("cart/",views.cart_summary,name="cart_summary"),

]
