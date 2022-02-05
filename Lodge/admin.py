from django.contrib import admin

# Register your models here.
from .models import Action, Role, User, Customer, Room_type, Room, Booking, Booking_room, Checkin, Checkout, Discount_type, Seasonal_discount, Bulk_discount, Checked_in_guest

class Room_typeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "room_type_desc" )

class RoomAdmin(admin.ModelAdmin):
    list_display = ("__str__", "room_type", "sleeps")


admin.site.register(Action)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Room_type, Room_typeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking)
admin.site.register(Booking_room)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Discount_type)
admin.site.register(Seasonal_discount)
admin.site.register(Bulk_discount)
admin.site.register(Checked_in_guest)

