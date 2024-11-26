from django.db import models
import uuid
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.
class SizeChoice(models.TextChoices):
    small = ("sm","Small")
    medium = ("md","Medium")
    large = ("lg","Large")


class Products(models.Model):
    name = models.CharField(max_length=550)
    desp = models.TextField()
    orgianal_price = models.IntegerField()
    discount_price = models.IntegerField()
    id = models.CharField(max_length=50,default=uuid.uuid4,primary_key=True,editable=False)
    colors = models.ManyToManyField("shop.Colors")
    size = MultiSelectField(choices=SizeChoice,max_length=255,default=SizeChoice.medium) 
    image1 = models.ImageField(upload_to="product_images/",default="watch.png")
    image2 = models.ImageField(upload_to="product_images/",null=True,blank=True)
    image3 = models.ImageField(upload_to="product_images/",null=True,blank=True)
    image4 = models.ImageField(upload_to="product_images/",null=True,blank=True)


    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.user}: {self.product}"

class Colors(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=50,editable=False,default=uuid.uuid4,primary_key=True)

    def __str__(self):
        return self.name