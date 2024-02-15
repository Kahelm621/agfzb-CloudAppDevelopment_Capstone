from django.db import models
from django.utils.timezone import now


# In djangoapp/models.py

from django.db import models

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # __str__ method to print a car make object
    def __str__(self):
        return self.name

# CarModel model
class CarModel(models.Model):
    # Many-To-One relationship to CarMake model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()  # Refers to a dealer created in Cloudant database
    name = models.CharField(max_length=100)
    SEDAN = 'SEDAN'
    SUV = 'SUV'
    WAGON = 'WAGON'
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON'),
    ]
    car_type = models.CharField(max_length=50, choices=CAR_TYPE_CHOICES)
    year = models.DateField()

    # __str__ method to print the car model object
    def __str__(self):
        return f"{self.car_make.name} - {self.name}"
