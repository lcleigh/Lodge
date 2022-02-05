from datetime import timezone
from django.db import models
import datetime


# Create your models here.
class Action(models.Model): 
    BOOKING = 1
    CHECK = 2
    CANCEL = 3
    DISCOUNT = 4
    USERS = 5
    ROLE = (
        (BOOKING, ('Create bookings')),
        (CHECK, ('Check in/Check out')),
        (CANCEL, ('Cancel Bookings')),
        (DISCOUNT, ('Setup discounts')),
        (USERS, ('Manage users'))
    )
    allowed_actions = models.PositiveSmallIntegerField(
       choices=ROLE)

class Role(models.Model): 
    MANAGER = 1
    ASSMANAGER = 2
    CSA = 3
    ROLE_TYPE = (
        (MANAGER, ('Manager')),
        (ASSMANAGER, ('Assistant Manager')),
        (CSA, ('Customer Service Assistant'))
    )
    role_type = models.PositiveSmallIntegerField(choices=ROLE_TYPE)
    allowed_actions = models.ManyToManyField(Action)

class User(models.Model):
    full_name = models.CharField(max_length=240, null=False, blank=False)
    username = models.CharField(max_length=240)
    password = models.CharField(max_length=240)
    role_id = models.ForeignKey(Role, on_delete=models.PROTECT)
    created_at = models.DateTimeField (auto_now_add=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.CharField(max_length=240, blank = True, null = True)
    #TO DO checkin = models.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room_type(models.Model):
    LODGE = 'LX'
    DOUBLE = 'DB'
    SINGLE = 'SG'
    FAMILY = 'FM'
    ROOM_TYPE_DESC = (
        (LODGE, ('Luxury Lodge Room')),
        (DOUBLE, ('Standard Double')),
        (SINGLE, ('Single')),
        (FAMILY, ('Family Room'))
    )
    room_type_desc = models.CharField(max_length=40, choices = ROOM_TYPE_DESC)
    #room_type_desc = models.IntegerField(choices = ROOM_TYPE_DESC)
    max_occupancy = models.IntegerField

    def __str__(self):
        return f"{self.room_type_desc}"

class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.ForeignKey(Room_type, on_delete=models.PROTECT)
    sleeps = models.IntegerField()
    #floor = models.IntegerField()
    #cot = models.IntegerField(blank = True, null=True)
    #disabled_access = models.IntegerField(blank = True,null=True)
    #room_price = models.DecimalField(blank = True, decimal_places=2, max_digits=6)

    def __str__(self):
        return f"{self.room_number} {self.room_type}"

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

class Booking_room(models.Model): 
    booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)
    room_id = models.ForeignKey(Room, on_delete=models.PROTECT, default=0)

    def __str__(self):
        return f"{self.room_id}"

class Checkin(models.Model):
    #room_number = models.ForeignKey(Booking_room, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)
    checkin_date = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, default=0)
    
    def __str__(self):
        return f"{self.booking_id} {self.customer_id}"

class Checked_in_guest(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.customer_id}"

class Checkout(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)
    checkout_date = models.DateField(auto_now_add=True)

class Discount_type(models.Model):
    POUNDS = 1
    PERCENTAGE = 2
    
    TYPE = (
        (POUNDS, ('£')),
        (PERCENTAGE, ('%'))
    )
    type = models.PositiveSmallIntegerField(choices = TYPE)

class Seasonal_discount(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    seasonal_amount = models.DecimalField(decimal_places=2, max_digits=6)
    type_id = models.IntegerField(default = 0)

class Bulk_discount(models.Model):
    min_rooms = models.IntegerField()
    bulk_amount = models.DecimalField(decimal_places=2, max_digits=6)
    type_id = models.IntegerField(default = 0)


