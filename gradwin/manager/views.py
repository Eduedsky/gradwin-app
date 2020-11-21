from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register_employee(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register_employee')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register_employee')

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print('employee created')
                return redirect('manager_dashboard')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register_employee')
        return redirect('manager/manager_dashboard')

    else:
        return render(request, 'manager/register_employee.html')


def manager_dashboard(request):
    return render(request, 'manager/manager_dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('manager_signin')
