"""
mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', admin.site.urls),
    path("admin/", admin.site.urls),
    path("cars/", get_cars),
    path("customers/", get_customers),
    path("save_customer/", save_customer),
    path("delete_customer/<int:id>", delete_customer),
    path("update_customer/<int:id>", update_customer),
    path("save_car/", save_car),
    path("update_car/<int:id>", update_car),
    path("delete_car/<int:id>", delete_car),
    path("order_car/", order_car),
    path("rent_car/", rent_car),
    path("employees/", get_employees),
    path("save_employee/", save_employee),
    path("update_employee/<int:id>", update_employee),
    path("delete_employee/<int:id>", delete_employee),
    path("cancel_order/", cancel_ordered_car),
    path("return_car/", return_car),

]
