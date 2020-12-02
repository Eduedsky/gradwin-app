from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User, auth
from django.utils.text import slugify

# from django_slugify_processors.text import slugify

# from djmoney.models.fields import MoneyField
# from djmoney.money import Money


# Create your models here.

class Category(models.Model):
    # category_id = models.AutoField(primary_key=True, default=1, null=True)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering: ['-name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    # product_id = models.AutoField(primary_key=True, default=1, null=True)
    category = models.CharField(max_length=150)
    employee_username = models.CharField(
        max_length=150, null=True, blank=True, default='admin')
    serialno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    buying_price = models.FloatField()
    actual_price = models.FloatField(
        null=True, blank=True, default=1)
    selling_price = models.FloatField(
        null=True, blank=True, default=1)
    author = models.CharField(max_length=50, null=True, blank=True)
    VAT = models.FloatField(default=16)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_entry = models.DateTimeField(default=now)
    date_updated = models.DateTimeField(default=now)
    total_price_per_inventory = models.FloatField(
        null=True, blank=True, default=1)
    total_vat_per_inventory = models.FloatField(
        null=True, blank=True, default=1)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return self.name


# class OrderItem(models.Model):
#     product = models.ForeignKey(
#         Product, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(
#         Order, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering: ['-date']
