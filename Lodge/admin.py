from django.contrib import admin

# Register your models here.
from .models import Customer, Booking, Checkin



admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Checkin)
