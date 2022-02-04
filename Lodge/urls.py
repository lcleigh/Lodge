from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkin", views.checkin, name="checkin"),
    path("<int:flight_id>/book", views.book, name="book")
]