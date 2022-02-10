from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("checkin/<int:checkin_id>", views.checkin, name="checkin"),
    path("checkin/<int:checkin_id>/book", views.book, name="book"),
    path("checkout/<int:checkout_id>", views.checkout, name="checkout"),
    path("checkout/<int:checkout_id>/unbook", views.unbook, name="unbook"),
    path("home/", views.index, name="home"),
    path("check/", views.check, name="check"),
    path("booking/", views.booking, name="booking"),
    path("room/", views.room, name="room")
    #path("dashboard/", views.contact, name="dashboard")
]
    

urlpatterns += staticfiles_urlpatterns()