from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from . models import CustomUser, Vendor, Inventory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, VendorForm, InventoryForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user 

    custom_user = CustomUser.objects.filter(user_id=current_user.id).first()

    if custom_user is None:
        return HttpResponseRedirect('profile')

    inventory = None
    vendor = None
    if custom_user.user_type == 'vendor':
        vendor = Vendor.objects.filter(custom_user_id = custom_user.id).first()

        if vendor is None:
            return HttpResponseRedirect('/vendor')

        inventory = Inventory.objects.filter(vendor_id = vendor.id)
        
    return render(request, 'index.html',{'custom_user': custom_user, 'vendor': vendor, 'inventory':inventory})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.user = current_user
            custom_user.save()

            if custom_user.user_type == 'vendor':
                return HttpResponseRedirect('/vendor')
            else:
                return HttpResponseRedirect('/')
    else:
        form = CustomUserForm()

    return render(request, 'add_profile.html', {"form": form})


def check_profile(request):
    current_user = request.user

    custom_user = CustomUser.objects.filter(user_id=current_user.id).first()

    if custom_user is None:
        return HttpResponseRedirect('profile'), custom_user, None

    vendor = None
    if custom_user.user_type == 'vendor':
        vendor = Vendor.objects.filter(custom_user_id = custom_user.id).first()

        if vendor is None:
            return HttpResponseRedirect('/'), custom_user, None

    return None, custom_user, vendor

@login_required(login_url='/accounts/login/')
def add_vendor(request):
    current_user = request.user

    redirect, custom_user, vendor = check_profile(request)

    if vendor is not None:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)            
            vendor.custom_user = custom_user
            vendor.save()

            return HttpResponseRedirect('/')

    else:
        form = VendorForm()

    return render(request, 'vendor.html', {"form": form})


@login_required(login_url='/accounts/login/')
def add_flower(request):
    current_user = request.user

    redirect, custom_user, vendor = check_profile(request)

    if redirect is not None:
        return redirect


    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            flower = form.save(commit=False)            
            flower.vendor = vendor
            flower.save()

            return HttpResponseRedirect('/')

    else:
        form = InventoryForm()

    return render(request, 'add_flower.html', {"form": form})

def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_flower_shop = Vendor.search_by_address(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"flower_shops": searched_flower_shop})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})