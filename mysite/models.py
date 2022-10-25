from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.IntegerField()
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' ' + self.carmodel + self.year + " " + self.location + ", " + self.status


class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name + self.year + self.branch


class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.age + ", " + self.address
