from django.urls import path
from . import views

urlpatterns = [
    path('sales_dashboard', views.sales_dashboard,
         name="sales_dashboard"),
    path('logout', views.logout, name="logout"),

]
