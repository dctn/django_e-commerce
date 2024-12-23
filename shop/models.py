from django.db import models
import uuid
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField
# Create your models here.
class SizeChoice(models.TextChoices):
    small = ("Small","Small")
    medium = ("Medium","Medium")
    large = ("Large","Large")


class Products(models.Model):
    name = models.CharField(max_length=550)
    desp = models.TextField()
    orgianal_price = models.IntegerField()
    discount_price = models.IntegerField()
    id = models.CharField(max_length=50,default=uuid.uuid4,primary_key=True,editable=False)
    colors = models.ManyToManyField("shop.Colors")
    size = MultiSelectField(choices=SizeChoice,max_length=255,default=SizeChoice.medium) 
    image1 = CloudinaryField("image")
    image2 = CloudinaryField("image")
    image3 = CloudinaryField("image")
    image4 = CloudinaryField("image")


    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    color = models.CharField(max_length=550,default="")
    Size = models.CharField(max_length=550,default="medium")
    quantity = models.IntegerField()
    id_test = models.CharField(max_length=50,default="",editable=False)
    
    def __str__(self):
        return f"{self.user}: {self.product}"

class Colors(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=50,editable=False,default=uuid.uuid4,primary_key=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.CharField(max_length=500)
    size = models.CharField(max_length=500,)
    color = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.PROTECT,default="")
    id = models.CharField(max_length=550,default=uuid.uuid4,editable=False,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user}: {self.product}"