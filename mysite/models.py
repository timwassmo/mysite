from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.DateField()


    def __str__(self):
        return self.make + ' ' + self.carmodel