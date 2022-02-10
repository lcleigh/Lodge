from datetime import timezone
from django.db import models
import datetime


# Create your models here.

class Checkin(models.Model):
    checkin_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.checkin_date}"


class Checkout(models.Model):  
    checkout_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.checkout_date}"


class Customer(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.CharField(max_length=240, blank = True, null = True)
    checkins = models.ManyToManyField(Checkin, blank=True, related_name="customers")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Guest(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.CharField(max_length=240, blank = True, null = True)
    checkouts = models.ManyToManyField(Checkout, blank=True, related_name="guests")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
