from django.urls import path
from . import views

urlpatterns = [
    path('sales_dashboard', views.sales_dashboard,
         name="sales_dashboard"),
    path('logout', views.logout, name="logout"),
    path('order/<int:serialno>', views.order, name="order"),
    path('search_product', views.search_product, name="search_product"),
    path('export_orders_csv', views.export_orders_csv, name='export_orders_csv'),
    path('sales_view_by_date_entry', views.sales_view_by_date_entry,
         name='sales_view_by_date_entry'),
    path('sales_view_by_name', views.sales_view_by_name, name='sales_view_by_name'),
    path('sales_view_by_author', views.sales_view_by_author,
         name='sales_view_by_author'),

    path('sales_view_by_highest_price', views.sales_view_by_highest_price,
         name='sales_view_by_highest_price'),
    path('sales_view_by_lowest_price', views.sales_view_by_lowest_price,
         name='sales_view_by_lowest_price'),




]
