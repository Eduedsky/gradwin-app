from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('manager_signin', views.manager_sign_in, name="manager_signin"),
    path('inventory_signin', views.inventory_sign_in, name="inventory_signin"),
    path('sales_signin', views.sales_sign_in, name="sales_signin"),
    path('logout', views.logout, name="logout"),

]
