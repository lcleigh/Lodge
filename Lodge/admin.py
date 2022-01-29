from django.contrib import admin

# Register your models here.
from .models import Actions
from .models import Roles
from .models import Users
from .models import Customers
from .models import Room_type
from .models import Rooms
from .models import Bookings
from .models import Booking_rooms
from .models import Checkin
from .models import Checkout
from .models import Discount_type
from .models import Seasonal_discounts
from .models import Bulk_discounts

admin.site.register(Actions)
admin.site.register(Roles)
admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Room_type)
admin.site.register(Rooms)
admin.site.register(Bookings)
admin.site.register(Booking_rooms)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Discount_type)
admin.site.register(Seasonal_discounts)
admin.site.register(Bulk_discounts)