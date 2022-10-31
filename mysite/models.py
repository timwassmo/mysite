from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' ' + self.carmodel +", "+ self.year + ". " + self.location + ", " + self.status


class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.address + " " + self.branch


class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    active_order = models.BooleanField(default = False)

    def __str__(self):
        return self.name + " " + str(self.age) + ", " + self.address

class Order(models.Model):
    car = models.IntegerField()
    customer = models.IntegerField()

    def __str__(self):
        return str(self.car) + " " + str(self.customer)
