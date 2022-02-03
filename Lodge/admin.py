from django.contrib import admin

# Register your models here.
from .models import Action
from .models import Role
from .models import User
from .models import Customer
from .models import Room_type
from .models import Room
from .models import Booking
from .models import Booking_room
from .models import Checkin
from .models import Checkout
from .models import Discount_type
from .models import Seasonal_discount
from .models import Bulk_discount

admin.site.register(Action)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Room_type)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Booking_room)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Discount_type)
admin.site.register(Seasonal_discount)
admin.site.register(Bulk_discount)