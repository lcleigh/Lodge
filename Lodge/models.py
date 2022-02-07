from datetime import timezone
from django.db import models

# Create your models here.
class Actions(models.Model): 
    allowed_actions = models.CharField(max_length=240)

class Roles(models.Model): 
    role_type_desc = models.CharField(max_length=240)
    allowed_actions = models.ManyToManyField(Actions)

class Users(models.Model):
    full_name = models.CharField(max_length=240, null=False, blank=False)
    username = models.CharField(max_length=240)
    password = models.CharField(max_length=240)
    role_id = models.ForeignKey(Roles, on_delete=models.PROTECT)
    created_at = models.DateTimeField (auto_now_add=True)

class Customers(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.CharField(max_length=240, blank = True, null = True)

class Room_type(models.Model):
    room_type_desc = models.CharField(max_length=240)
    max_occupancy = models.IntegerField

class Rooms(models.Model):
    room_number = models.IntegerField()
    room_type = models.ForeignKey(Room_type, on_delete=models.PROTECT, related_name='room_type')
    sleeps = models.IntegerField()
    floor = models.IntegerField()
    cot = models.IntegerField()
    disabled_access = models.IntegerField()
    room_price = models.DecimalField(decimal_places=2, max_digits=6)

class Bookings(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.PROTECT, related_name='customers')
    first_date = models.DateTimeField()
    last_date = models.DateTimeField()
    booked_date = models.DateTimeField()
    adults = models.IntegerField()
    children = models.IntegerField()
    cancellation_date = models.DateTimeField(blank = True, null = True)

    def booked(self):
        self.booked_date = timezone.now()
        self.save()

class Booking_rooms(models.Model): 
    booking_id = models.ForeignKey(Bookings, on_delete=models.PROTECT, related_name='rooms_booked')
    room_id = models.ForeignKey(Rooms, on_delete=models.PROTECT)

class Checkin(models.Model):
    booking_room_id = models.ForeignKey(Booking_rooms, on_delete=models.PROTECT, related_name='checkin')
    checkin_date = models.DateTimeField(auto_now_add=True)
 
class Checkout(models.Model):
    booking_room_id = models.ForeignKey(Booking_rooms, on_delete=models.PROTECT)
    checkout_date = models.DateTimeField(auto_now_add=True)

class Discount_type(models.Model):
    type = models.CharField(max_length=240)

class Seasonal_discounts(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    seasonal_amount = models.DecimalField(decimal_places=2, max_digits=6)
    type_id = models.IntegerField(default = 0)

class Bulk_discounts(models.Model):
    min_rooms = models.IntegerField()
    bulk_amount = models.DecimalField(decimal_places=2, max_digits=6)
    type_id = models.IntegerField(default = 0)