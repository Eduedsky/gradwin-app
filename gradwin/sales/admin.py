from django.contrib import admin
from .models import Order, Credit_Customer, Payment_method, Paid_Order


# Register your models here.
admin.site.register(Order)
admin.site.register(Credit_Customer)
admin.site.register(Payment_method)
admin.site.register(Paid_Order)
