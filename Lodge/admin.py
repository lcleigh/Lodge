from django.contrib import admin

# Register your models here.
from .models import Customer, Checkin, Checkout, Guest


class CustomerAdmin(admin.ModelAdmin):
    filter_horizontal = ("checkins",)


class GuestAdmin(admin.ModelAdmin):
    filter_horizontal = ("checkouts",)  
   


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Guest, GuestAdmin)
