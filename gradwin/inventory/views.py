import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.db.utils import OperationalError
from django.core.paginator import Paginator
from datetime import datetime
from django.urls import reverse


# Create your views here.


@login_required(login_url='inventory_signin')
def inventory_dashboard(request):
    product = Product.objects.all()
    categories = Category.objects.all()

    quantity = 0
    for quantities in product:
        quantity = quantity + quantities.quantity
    vat = 0
    for tax in product:
        vat_times_quantity = tax.VAT * tax.quantity
        vat = vat + vat_times_quantity

    total_price = 0
    for price in product:
        price_times_quantity = price.buying_price * price.quantity
        total_price = total_price + price_times_quantity

    context = {
        'categories': categories,
        'values': request.POST,
        'product': product,
        'quantity': quantity,
        'vat': vat,
        'total_price': total_price,
    }

    if request.method == 'GET':

        return render(request, 'inventory/inventory_dashboard.html', context)


@login_required(login_url='inventory_signin')
def add_inventory(request):
    category = Category.objects.all()
    context = {
        'category': category,
        'values': category
    }

    if request.method == 'GET':
        return render(request, 'inventory/add_inventory.html', context)

    if request.method == 'POST':
        context = {
            'category': category,
            'values': request.POST,
        }
        quantity = request.POST['quantity']
        name = request.POST['name']
        author = request.POST['author']
        buying_price = request.POST['buying_price']
        category = request.POST['category']
        employee_username = request.user.username
        VAT = float(buying_price) * float(0.16)
        total_price_per_inventory = float(buying_price) * float(quantity)
        total_vat_per_inventory = float(quantity) * float(VAT)
        Product.objects.create(name=name, buying_price=buying_price, employee_username=employee_username, total_vat_per_inventory=total_vat_per_inventory,
                               quantity=quantity, author=author, category=category, VAT=VAT, total_price_per_inventory=total_price_per_inventory)

        messages.success(request, 'Inventory Added succesfuly')
        return redirect('view_inventory')

    else:
        return render(request, 'inventory/add_inventory.html')


@login_required(login_url='inventory_signin')
def add_category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    if request.method == 'GET':
        return render(request, 'inventory/add_category.html', context)

    if request.method == 'POST':
        name = request.POST['name']

        if Category.objects.filter(name=name).exists():
            messages.error(request, 'Category Already Exists')
            return redirect('add_category')
        else:
            Category.objects.create(name=name)
            messages.success(request, 'Category Added succesfuly')
            return redirect('add_inventory')

    else:
        return render(request, 'inventory/add_category.html')


@login_required(login_url='inventory_signin')
def delete_category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    if request.method == 'GET':
        return render(request, 'inventory/delete_category.html', context)

    if request.method == 'POST':
        search_field = request.POST['search_field']
        if search_field == '':
            return redirect('delete_category')

        category = Category.objects.filter(name__contains=search_field)
        context = {
            'category': category,
            'values': request.POST
        }

        if category.exists():
            messages.info(request, 'Search Results')
            category.delete()
            messages.success(request, "Category Deleted Succesfuly")
            return render(request, 'inventory/delete_category.html', context)
        else:
            messages.error(request, 'Category Not found!')
            return render(request, 'inventory/delete_category.html', context)
    else:
        return render(request, 'inventory/delete_category.html', context)


@login_required(login_url='inventory_signin')
def delete_inventory(request, id):
    product = Product.objects.get(pk=id)

    product.delete()
    messages.success(request, "Product Deleted Succesfuly")
    return redirect('view_inventory')


@login_required(login_url='inventory_signin')
def view_inventory(request):
    product = Product.objects.all()
    # paginator = Paginator(product, 5)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, 1)
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'inventory/view_inventory.html', context)


@login_required(login_url='inventory_signin')
def edit_product(request, id):
    product = Product.objects.get(pk=id)
    category = Category.objects.all()

    context = {
        'product': product,
        'category': category,
        'values': product,
    }

    if request.method == 'GET':
        return render(request, 'inventory/edit_product.html', context)

    if request.method == 'POST':
        quantity = request.POST['quantity']
        name = request.POST['name']
        author = request.POST['author']
        buying_price = request.POST['buying_price']
        category = request.POST['category']
        employee_username = request.user.username
        VAT = float(buying_price) * float(0.16)
        date_updated = datetime.now()
        total_price_per_inventory = float(buying_price) * float(quantity)
        total_vat_per_inventory = float(quantity) * float(VAT)

        product.quantity = quantity
        product.name = name
        product.author = author
        product.date_updated = date_updated
        product.buying_price = buying_price
        product.category = category
        product.employee_username = employee_username
        product.VAT = VAT
        product.total_price_per_inventory = total_price_per_inventory
        product.total_vat_per_inventory = total_vat_per_inventory

        product.save()
        # return render(request, 'inventory/edit_product.html', context)
        messages.success(request, "Inventory Details Updated Successfuly")
        return redirect('view_inventory')


@login_required(login_url='inventory_signin')
def view_by_date_entry(request):
    product = Product.objects.order_by('-date_entry')

    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'inventory/view_inventory.html', context)


@login_required(login_url='inventory_signin')
def view_by_name(request):
    product = Product.objects.order_by('-name')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'inventory/view_inventory.html', context)


@login_required(login_url='inventory_signin')
def view_by_author(request):
    product = Product.objects.order_by('-author')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'inventory/view_inventory.html', context)


@login_required(login_url='inventory_signin')
def view_by_lowest_price(request):
    product = Product.objects.order_by('buying_price')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'inventory/view_inventory.html', context)


@login_required(login_url='inventory_signin')
def view_by_highest_price(request):
    product = Product.objects.order_by('-buying_price')
    context = {
        'product': product,
    }
    if request.method == 'GET':
        return render(request, 'inventory/view_inventory.html', context)


@login_required(login_url='inventory_signin')
def export_product_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Serial Number', 'Product Name',
                     'Price', 'Date Entered'])

    product = Product.objects.all().values_list(
        'serialno', 'name', 'price', 'date_entry')
    for product in product:
        writer.writerow(product)

    return response


def search_product(request):
    context = {
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'inventory/search_product.html')

    if request.method == 'POST':
        search_field = request.POST['search_field']
        if search_field == '':
            return redirect('view_inventory')

        product = Product.objects.filter(name__contains=search_field)

        context = {
            'product': product,
            'values': request.POST
        }

        if product.exists():
            messages.info(request, 'Search Results')
            return render(request, 'inventory/search_product.html', context)
        else:
            messages.error(request, 'Product Not found!')
            return render(request, 'inventory/search_product.html', context)
    else:
        return render(request, 'inventory/search_product.html', context)


# def search_product_filter_by_date(request):
#     if request.method == 'GET':
#         search_field = request.GET['search_field']
#         product = Product.objects.filter(name__contains=search_field)
#         product = product.objects.order_by('-date_entry')

#         context = {
#             'product': product,
#             'values': request.POST
#         }
#         return render(request, 'inventory/view_inventory.html', context)
#     else:
#         return render(request, 'inventory/view_inventory.html', context)


def logout(request):
    auth.logout(request)
    return redirect('inventory_signin')

    # @login_required(login_url='inventory_signin')
    # def product_details(request, category_slug, slug):
    #     product = get_object_or_404(Product, slug=slug)

    #     context = {
    #         'product': product
    #     }
    #     return render(request, 'inventory/inventory_management.html', context)

    # @login_required(login_url='inventory_signin')
    # def category_details(request, slug):
    #     category = get_object_or_404(Category, slug=slug)
    #     product = category.products.all()

    #     context = {
    #         'product': product,
    #         'category': category
    #     }
    #     return render(request, 'inventory/inventory_management.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        return render(request, 'shop/product/list.html',  {'category': category, 'categories': categories,  'products': products})
