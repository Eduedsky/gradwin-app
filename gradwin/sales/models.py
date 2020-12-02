from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User, auth


# Create your models here.
class Payment_method(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering: ['-name']

    def __str__(self):
        return self.name


class Credit_Customer(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)
    customer_id = models.IntegerField(auto_created=True, unique=True)
    paid = models.BooleanField(default=False)
    mode_of_payment = models.ForeignKey(
        Payment_method, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=13)

    class Meta:
        ordering: ['-first_name']

    def __str__(self):
        return self.first_name + '|' + str(self.second_name)


class Order(models.Model):
    customer = models.ForeignKey(
        Credit_Customer, on_delete=models.CASCADE)
    transaction_id = models.IntegerField(
        auto_created=True, default=1)
    employee_id = models.IntegerField(null=True, blank=True)
    serialno = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    buying_price = models.FloatField(null=True, blank=True, )
    selling_price = models.FloatField(
        null=True, blank=True, default=buying_price)
    author = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    VAT = models.FloatField(default=16)
    profit = models.FloatField(null=True, blank=True, default=0)
    loss = models.FloatField(null=True, blank=True, default=0)
    date_entry = models.DateTimeField(default=now)
    paid = models.BooleanField(default=False)
    mode_of_payment = models.ForeignKey(
        Payment_method, on_delete=models.PROTECT)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.name)


class Paid_Order(models.Model):
    customer = models.ForeignKey(
        Credit_Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    paid = models.BooleanField(default=True, null=True, blank=False)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.name)
