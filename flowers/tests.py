from django.test import TestCase
from .models import CustomUser, Vendor, Inventory, User

# Create your tests here.

class CustomUserTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.feven = CustomUser(first_name='feven', last_name = 'moghes', telephone= 0-119140, profile_pic = '/home/feven/Pictures/Moringa_pics', user_type = 'Vendor',has_profile = True, user = user)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.feven, CustomUser))

    # Testing Save Method
    def test_save_method(self):
        self.feven.save_customuser()
        custome_users = CustomUser.objects.all()
        self.assertTrue(len(custome_users) > 0)

    # Testing delete method
    def tearDown(self):
        CustomUser.delete_customuser




class VendorTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.feven = CustomUser(first_name='feven', last_name = 'moghes', telephone= 0-119140, profile_pic = '/home/feven/Pictures/Moringa_pics', user_type = 'Vendor',has_profile = True, user = user)
        self.feven.save_customuser()
        self.flora = Vendor(shop_name='flora', shop_address= 'yaya', telephone=0-119140, contact_name= 'simon',deliver_online='True', profile_pic = '/home/feven/Pictures/Moringa_pics', custom_user=self.feven)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.flora, Vendor))

    # Testing Save Method
    def test_save_method(self):
        self.flora.save_vendor()
        flower_shop = Vendor.objects.all()
        self.assertTrue(len(flower_shop) > 0)

    # Testing delete method
    def tearDown(self):
        Vendor.delete_vendor



class InventoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.feven = CustomUser(first_name='feven', last_name = 'moghes', telephone= 0-119140, profile_pic = '/home/feven/Pictures/Moringa_pics', user_type = 'Vendor',has_profile = True, user = user)
        self.feven.save_customuser()
        self.flora = Vendor(shop_name='flora', shop_address= 'yaya', telephone=0-119140, contact_name= 'simon',deliver_online='True', profile_pic = '/home/feven/Pictures/Moringa_pics', custom_user=self.feven)
        self.flora.save_vendor()
        self.red = Inventory(flower_color='red', quantity=5, unitprice=200, flower_pic='/home/feven/Pictures/Moringa_pics', vendor=self.flora)


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.red, Inventory))

    # Testing Save Method
    def test_save_method(self):
        self.red.save_inventory()
        inventories = Inventory.objects.all()
        self.assertTrue(len(inventories) > 0)

    # Testing delete method
    def tearDown(self):
        Inventory.delete_inventory










