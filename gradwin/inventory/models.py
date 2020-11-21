from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money

# Create your models here.


class Inventory(models.Model):

    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pics', null=True, blank=True)
    quantity = models.IntegerField()
    price = MoneyField(decimal_places=2, max_digits=12, default_currency='KSH')
    date_entry = models.DateTimeField(auto_now_add=True)
    date_sold = models.DateTimeField(null=True, blank=True)
