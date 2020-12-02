from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from inventory.models import Product
from django.db.utils import OperationalError
from sales.models import Order
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv


# Create your views here.

@login_required(login_url='sales_signin')
def sales_dashboard(request):
    order = Order.objects.order_by('-date_entry')
    context = {
        'order': order
    }

    if request.method == 'GET':
        return render(request, 'sales/sales_dashboard.html', context)


@login_required(login_url='sales_signin')
def order(request, serialno):
    # order = Order.objects.all()
    product = Product.objects.get(pk=serialno)
    context = {
        'product': product,
        'values': product,
        # 'order': order,
    }

    if request.method == 'GET':
        return render(request, 'sales/order.html', context)

    if request.method == 'POST':
        name = product.name
        serialno = product.serialno
        price = product.price
        author = product.author

        order.name = name
        order.serialno = serialno
        order.price = price
        order.author = author

        Order.objects.create(name=name, author=author,
                             serialno=serialno, price=price)
        product.delete()
        messages.success(request, "Product Sold Succesfuly")
        return redirect('sales_dashboard')


def search_product(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'sales/search_product.html', context)

    if request.method == 'POST':
        search_field = request.POST['search_field']

        if search_field == '':
            return redirect('search_product')
        product = Product.objects.filter(name__contains=search_field)

        context = {
            'product': product,
            'values': request.POST
        }

        if product.exists():
            messages.info(request, 'Search Results')
            return render(request, 'sales/search_product.html', context)
        else:
            messages.error(request, 'Product Not found!')
            return render(request, 'sales/search_product.html', context)
    else:
        return render(request, 'sales/search_product.html', context)


@login_required(login_url='sales_signin')
def export_orders_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Serial Number', 'Product Name',
                     'Price', 'Date Ordered'])

    order = Order.objects.all().values_list(
        'serialno', 'name', 'price', 'date_entry')
    for order in order:
        writer.writerow(order)

    return response


@login_required(login_url='sales_signin')
def sales_view_by_date_entry(request):
    product = Product.objects.order_by('-date_entry')

    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'sales/search_product.html', context)


@login_required(login_url='sales_signin')
def sales_view_by_name(request):
    product = Product.objects.order_by('-name')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'sales/search_product.html', context)


@login_required(login_url='sales_signin')
def sales_view_by_author(request):
    product = Product.objects.order_by('-author')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'sales/search_product.html', context)


@login_required(login_url='sales_signin')
def sales_view_by_lowest_price(request):
    product = Product.objects.order_by('price')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'sales/search_product.html', context)


@login_required(login_url='sales_signin')
def sales_view_by_highest_price(request):
    product = Product.objects.order_by('-price')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'sales/search_product.html', context)


def logout(request):
    auth.logout(request)
    return redirect('sales_signin')
