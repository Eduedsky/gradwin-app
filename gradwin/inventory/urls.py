from django.urls import path
from . import views

urlpatterns = [
    path('inventory_dashboard', views.inventory_dashboard,
         name="inventory_dashboard"),
    path('add_inventory', views.add_inventory, name="add_inventory"),
    path('add_category', views.add_category, name="add_category"),
    path('delete_inventory/<int:id>',
         views.delete_inventory, name="delete_inventory"),
    path('delete_category', views.delete_category, name="delete_category"),

    path('view_inventory', views.view_inventory, name="view_inventory"),
    path('edit_product/<int:id>', views.edit_product, name="edit_product"),
    path('export_product_csv', views.export_product_csv, name='export_product_csv'),
    path('view_by_date_entry', views.view_by_date_entry, name='view_by_date_entry'),
    path('view_by_name', views.view_by_name, name='view_by_name'),
    path('view_by_author', views.view_by_author, name='view_by_author'),

    path('view_by_highest_price', views.view_by_highest_price,
         name='view_by_highest_price'),
    path('view_by_lowest_price', views.view_by_lowest_price,
         name='view_by_lowest_price'),
    path('search_product', views.search_product, name="search_product"),

    path('logout', views.logout, name="logout"),


]
