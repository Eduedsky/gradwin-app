from django.urls import path
from . import views


urlpatterns = [
    path('manager_dashboard', views.manager_dashboard, name="manager_dashboard"),
    path('register_employee', views.register_employee, name="register_employee"),
    path('logout', views.logout, name="logout"),

]
