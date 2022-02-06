from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkin", views.checkin, name="checkin"), 
    path("home/", views.contact, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signin/", views.contact, name="signin")
]

urlpatterns += staticfiles_urlpatterns()