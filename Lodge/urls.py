from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkin/<int:checkin_id>", views.checkin, name="checkin"),
    path("checkin/<int:checkin_id>/book", views.book, name="book"),
    path("checkout/<int:checkout_id>", views.checkout, name="checkout"),
    path("checkout/<int:checkout_id>/unbook", views.unbook, name="unbook"),
    path("home/", views.contact, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signin/", views.contact, name="signin")
]
    

urlpatterns += staticfiles_urlpatterns()