from django.db import models
import uuid
from multiselectfield import MultiSelectField
from PIL import Image
from io import BytesIO
import os
from django.core.files.uploadedfile import InMemoryUploadedFile

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
    id = models.CharField(max_length=50,default=uuid.uuid4,primary_key=True)
    size = MultiSelectField(choices=SizeChoice,max_length=255,default=SizeChoice.medium) 
    image1 = models.ImageField(upload_to="product_images/",default="watch.png")
    image2 = models.ImageField(upload_to="product_images/",null=True,blank=True)
    image3 = models.ImageField(upload_to="product_images/",null=True,blank=True)
    image4 = models.ImageField(upload_to="product_images/",null=True,blank=True)


    def __str__(self):
        return self.name
    
