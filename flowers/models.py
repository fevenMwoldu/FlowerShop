from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    customer_name= models.CharField(max_length=30)
    telephone = models.CharField(max_length = 20)
    profile_pic = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User)

    def __str__(self):
        return 'Customer (customer_name: {self.customer_name}, telephone: {self.telephone})'.format(self=self)

    def save_customer(self):
        self.save()

    def delete_customer(self):
        self.delete()


class Seller(models.Model):
    shop_name= models.CharField(max_length=30)
    shop_address= models.CharField(max_length=30)
    telephone = models.CharField(max_length = 20)
    contact_name= models.CharField(max_length=30)
    deliver_online = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User)

    def __str__(self):
        return 'Seller (shop_name: {self.shop_name}, shop_address: {self.shop_address}, telephone: {self.telephone}, contact_name:{self.contact_name})'.format(self=self)

    def save_seller(self):
        self.save()

    def delete_seller(self):
        self.delete()

class Inventory(models.Model):
    flower_color = models.CharField(max_length=10)
    quantity = models.IntegerField()
    unitprice = models.FloatField()
    profile_pic = models.ImageField(upload_to='photos/')
    seller = models.ForeignKey(Seller)
    

    def __str__(self):
        return 'Inventory (flower_color: {self.flower_color}, quantity: {self.quantity}, unitprice: {self.unitprice})'.format(self=self)

    def save_inventory(self):
        self.save()

    def delete_inventory(self):
        self.delete()