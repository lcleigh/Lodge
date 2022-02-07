from django.contrib import admin

# Register your models here.
from .models import Customer, Checkin


class CustomerAdmin(admin.ModelAdmin):
    filter_horizontal = ("checkins",)
    


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Checkin)
