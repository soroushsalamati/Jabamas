"""
The `Customer` model represents a customer in the application. It has a one-to-one relationship with the Django `User` model, and stores the customer's phone number and wallet balance.

The `Reserve` model represents a reservation made by a customer. It has a foreign key relationship with the `Customer` and `Owner` models, and stores the start and end times of the reservation.
"""
from django.db import models
from django.contrib.auth.models import User
from owner_app.models import Villa


class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=11)
    wallet = models.FloatField()


class Reserve(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.PROTECT)
    villa = models.ForeignKey(Villa , on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()