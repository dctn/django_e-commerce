from django.contrib import admin
from .models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","product","color","size"]
    search_fields = ["user","product","color","size"]
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Colors)
admin.site.register(Order,OrderAdmin)