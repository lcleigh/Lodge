from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("checkin", views.checkin, name="checkin"),
    path("checked_in", views.checked_in, name="checked_in"),
    path("checked_out", views.checked_out, name="checked_out"),
    path("home/", views.contact, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signin/", views.contact, name="signin")
]