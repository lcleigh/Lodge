from datetime import timezone
from django.db import models
import datetime



class Checkin(models.Model):
    #room_number = models.ForeignKey(Booking_room, on_delete=models.CASCADE)
    #booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)
    checkin_date = models.DateField(blank=True, null=True)
    #customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.checkin_date}"


class Customer(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.CharField(max_length=240, blank = True, null = True)
    checkin = models.ManyToManyField(Checkin, blank=True, related_name="customers")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    #room_number = models.ForeignKey(Booking_room, on_delete=models.PROTECT)
    first_date = models.DateField(blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    booked_date = models.DateField(blank=True, null=True)
    adults = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    cancellation_date = models.DateTimeField(blank=True, null=True)
    
    def booked(self):
        self.booked_date = timezone.now()
        self.save()
  

    def __str__(self):
        return f"{self.id}: {self.customer_id} {self.first_date} to {self.last_date}"
 


