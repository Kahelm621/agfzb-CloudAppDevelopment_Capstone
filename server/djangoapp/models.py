# models.py

from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you'd like for Car Make model

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()  # Refers to a dealer created in cloudant database
    TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices if needed
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()
    # Add any other fields you'd like for Car Model

    def __str__(self):
        return self.name

class CarDealer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(max_length=20)
    st = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)

    def __str__(self):
        return "Dealer name: " + self.full_name

class DealerReview(models.Model):
    dealer_id = models.IntegerField()
    review = models.TextField()
    review_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Review for Dealer ID: {self.dealer_id}"


