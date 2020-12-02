from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@login_required(login_url='manager_signin')
@staff_member_required
def register_employee(request):
    context = {
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'manager/register_employee.html', context)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return render(request, 'manager/register_employee.html', context)

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return render(request, 'manager/register_employee.html', context)

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Employee Created')
                return redirect('view_employee')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register_employee')
        return redirect('manager/manager_dashboard')

    else:
        return render(request, 'manager/register_employee.html')


@login_required(login_url='manager_signin')
@staff_member_required
def manager_dashboard(request):
    return render(request, 'manager/manager_dashboard.html')


@login_required(login_url='manager_signin')
@staff_member_required
def view_employee(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'manager/view_employee.html', context)


@login_required(login_url='manager_signin')
@staff_member_required
def edit_employee(request, id):
    user = User.objects.get(pk=id)
    context = {
        'user': user,
        'values': user,
    }

    if request.method == 'GET':
        return render(request, 'manager/edit_employee.html', context)

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user.username = username
        user.email = email
        user.save()
        # return render(request, 'inventory/edit_product.html', context)
        messages.success(
            request, "Employee Records Updated Successfuly")
        return redirect('view_employee')
    else:
        return render(request, 'manager/edit_employee.html', context)


# def del_user(request, username):
#     try:
#         u = User.objects.get(username=username)
#         u.delete()
#         messages.success(request, "The user is deleted")
#     except User.DoesNotExist:
#         messages.error(request, "User doesnot exist")
#         return render(request, 'view_employee.html')
#     except Exception as e:
#         return render(request, 'view_employee.html', {'err': e.message})
#     return render(request, 'view_employee.html')

@login_required(login_url='manager_signin')
@staff_member_required
def deactivate_user(request, id):
    user = User.objects.get(pk=id)
    context = {
        'user': user,
        'values': user,
    }
    user.is_active = False
    user.save()
    messages.success(request, user.first_name +
                     ' has been successfully Deactivated.')
    return redirect('view_employee')


@login_required(login_url='manager_signin')
@staff_member_required
def activate_user(request, id):
    user = User.objects.get(pk=id)
    context = {
        'user': user,
        'values': user,
    }
    user.is_active = True
    user.save()
    messages.success(request,  user.first_name +
                     ' has successfully Activated.')
    return redirect('view_employee')


def logout(request):
    auth.logout(request)
    return redirect('manager_signin')
