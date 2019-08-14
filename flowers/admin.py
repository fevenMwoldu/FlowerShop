from django.contrib import admin
from .models import Customer, Seller, Inventory

# Register your models here.

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Inventory)
