from django.db import models
from django.contrib.auth.models import User


# Create your models here.


users_type = (
    ('customer','CUSTOMER'),
    ('vendor', 'VENDOR'),
    
)


class CustomUser(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length = 20)
    profile_pic = models.ImageField(upload_to='photos/')
    user_type = models.CharField(max_length=8, choices=users_type, default='customer')
    has_profile = models.BooleanField(default = False)
    user = models.ForeignKey(User)
    

    def __str__(self):
        return 'CustomUser (first_name: {self.first_name}, last_name: {self.last_name}, telephone {self.telephone}, profile_pic: {self.profile_pic}, user_type:{self.user_type}, user: {self.user})'.format(self=self)

    def save_customuser(self):
        self.save()

    def delete_customuser(self):
        self.delete()

class Vendor(models.Model):
    shop_name= models.CharField(max_length=30)
    shop_address= models.CharField(max_length=30)
    telephone = models.CharField(max_length = 20)
    contact_name= models.CharField(max_length=30)
    deliver_online = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='photos/')
    custom_user = models.ForeignKey(CustomUser)

    def __str__(self):
        return 'Vendor (shop_name: {self.shop_name}, shop_address: {self.shop_address}, telephone: {self.telephone}, contact_name:{self.contact_name})'.format(self=self)

    def save_vendor(self):
        self.save()

    def delete_vendor(self):
        self.delete()

    @classmethod
    def search_by_address(cls,search_term):
        flower_shop = cls.objects.filter(shop_address__icontains=search_term) | cls.objects.filter(shop_name__icontains=search_term)
        return flower_shop
    

class Inventory(models.Model):
    flower_color = models.CharField(max_length=10)
    quantity = models.IntegerField()
    unitprice = models.FloatField()
    flower_pic = models.ImageField(upload_to='photos/')
    vendor = models.ForeignKey(Vendor)
    

    def __str__(self):
        return 'Inventory (flower_color: {self.flower_color}, quantity: {self.quantity}, unitprice: {self.unitprice})'.format(self=self)

    def save_inventory(self):
        self.save()

    def delete_inventory(self):
        self.delete()