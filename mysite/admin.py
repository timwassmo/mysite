from django.contrib import admin
from .models import Car, Customer, Employee

#Register car models

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Employee)

