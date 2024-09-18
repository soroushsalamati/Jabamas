"""
The `Villa` model represents a villa property, with fields for the neighborhood, address, description, capacity, and price.

The `Owner` model represents a villa owner, with fields for the owner's wallet balance and the villas they own. The `villa` field is a many-to-many relationship, allowing an owner to own multiple villas. The `user` field is a one-to-one relationship with the Django `User` model, linking the owner to a user account.
"""
from django.db import models
from django.contrib.auth.models import User


class Villa(models.Model):
    neighborhood =models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    price = models.FloatField()


class Owner(models.Model):
    wallet = models.FloatField()
    villa = models.ManyToManyField(Villa)
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    