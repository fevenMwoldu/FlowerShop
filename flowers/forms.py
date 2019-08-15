from django import forms
from .models import CustomUser, Vendor, Inventory

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['has_profile','user']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ['custom_user']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ['vendor']