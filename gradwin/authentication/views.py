from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


# class EmailValidationView(View):
#     def post(self, requests):
#         data = json.loads(requests.body)
#         email = data('email')


def index(request):
    return render(request, 'authentication/sign_in.html')


def sign_in(request):
    return render(request, 'authentication/sign_in.html')


def manager_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username='admin', password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('manager/manager_dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('manager_signin')

    else:
        return render(request, 'authentication/manager_signin.html')


def inventory_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('inventory/inventory_dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('inventory_signin')

    else:
        return render(request, 'authentication/inventory_signin.html')


def sales_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('sales/sales_dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('sales_signin')

    else:
        return render(request, 'authentication/sales_signin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
