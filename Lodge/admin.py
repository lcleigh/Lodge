from django.contrib import admin

# Register your models here.
from .models import Actions, Bookings, Roles, Users, Customers, Room_type, Rooms, Booking_rooms, Checkin, Checkout, Discount_type, Seasonal_discounts, Bulk_discounts

class Room_typeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "room_type_desc" )

class RoomAdmin(admin.ModelAdmin):
    list_display = ("__str__", "room_type", "sleeps")


admin.site.register(Actions)
admin.site.register(Roles)
admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Room_type, Room_typeAdmin)
admin.site.register(Rooms, RoomAdmin)
admin.site.register(Bookings)
admin.site.register(Booking_rooms)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Discount_type)
admin.site.register(Seasonal_discounts)
admin.site.register(Bulk_discounts)
