from django.contrib import admin
from .models import CustomUser,Vendor,Inventory

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Vendor)
admin.site.register(Inventory)
