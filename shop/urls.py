from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("products",views.products,name="products"),
    path("product_detail/<product_id>",views.product_details,name="product_details"),
    path("cart/",views.cart_summary,name="cart_summary"),
    path("cart_delete/<cart_id>",views.cart_delete,name="cart_delete"),
    path("contact/",views.contact,name="contact"),
    path("terms_conditions/",views.terms_conditions,name="terms_conditions"),

]
