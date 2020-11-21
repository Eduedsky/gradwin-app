from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Inventory

# Create your views here.


def inventory_dashboard(request):
    return render(request, 'inventory/inventory_dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('inventory_signin')
