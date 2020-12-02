from django.urls import path
from . import views


urlpatterns = [
    path('manager_dashboard', views.manager_dashboard, name="manager_dashboard"),
    path('register_employee', views.register_employee, name="register_employee"),
    path('view_employee', views.view_employee, name="view_employee"),
    path('edit_employee/<int:id>', views.edit_employee, name="edit_employee"),
    path('deactivate_user/<int:id>', views.deactivate_user, name="deactivate_user"),
    path('activate_user/<int:id>', views.activate_user, name="activate_user"),
    path('logout', views.logout, name="logout"),


]
