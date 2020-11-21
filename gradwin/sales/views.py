from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def sales_dashboard(request):
    return render(request, 'sales/sales_dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('sales_signin')
