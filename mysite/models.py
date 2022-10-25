from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.IntField()
    location = models.CharField(max_lenght=50)
    status = models.CharField(max_lenght=50)


    def __str__(self):
        return self.make + self.year + self.location + self.status + self.carmodel

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name + self.year + self.branch


