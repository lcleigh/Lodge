from datetime import timezone
from django.db import models

# Create your models here.
class Actions(models.Model): 
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

class Roles(models.Model): 
    MANAGER = 1
    ASSMANAGER = 2
    CSA = 3
    ROLE_TYPE = (
        (MANAGER, ('Manager')),
        (ASSMANAGER, ('Assistant Manager')),
        (CSA, ('Customer Service Assistant'))
    )
    role_type = models.PositiveSmallIntegerField(choices=ROLE_TYPE)
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
    LODGE = 1
    DOUBLE = 2
    SINGLE = 3
    FAMILY = 4
    ROOM_TYPE_DESC = (
        (LODGE, ('Luxury Lodge Room')),
        (DOUBLE, ('Standard Double')),
        (SINGLE, ('Single')),
        (FAMILY, ('Family Room'))
    )
    room_type_desc = models.PositiveSmallIntegerField(choices = ROOM_TYPE_DESC)
    max_occupancy = models.IntegerField

class Rooms(models.Model):
    room_number = models.IntegerField()
    room_type = models.ForeignKey(Room_type, on_delete=models.PROTECT)
    sleeps = models.IntegerField()
    floor = models.IntegerField()
    cot = models.IntegerField()
    disabled_access = models.IntegerField()
    room_price = models.DecimalField(decimal_places=2, max_digits=6)

class Bookings(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.PROTECT)
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
    booking_id = models.ForeignKey(Bookings, on_delete=models.PROTECT)
    room_id = models.ForeignKey(Rooms, on_delete=models.PROTECT, default=0)

class Checkin(models.Model):
    booking_id = models.ForeignKey(Bookings, on_delete=models.PROTECT)
    checkin_date = models.DateTimeField(auto_now_add=True)
 
class Checkout(models.Model):
    booking_id = models.ForeignKey(Bookings, on_delete=models.PROTECT)
    checkout_date = models.DateTimeField(auto_now_add=True)

class Discount_type(models.Model):
    POUNDS = 1
    PERCENTAGE = 2
    
    TYPE = (
        (POUNDS, ('£')),
        (PERCENTAGE, ('%'))
    )
    type = models.PositiveSmallIntegerField(choices = TYPE)

class Seasonal_discounts(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    seasonal_amount = models.DecimalField(decimal_places=2, max_digits=6)
    type_id = models.IntegerField(default = 0)

class Bulk_discounts(models.Model):
    min_rooms = models.IntegerField()
    bulk_amount = models.DecimalField(decimal_places=2, max_digits=6)
    type_id = models.IntegerField(default = 0)


