from asyncio.windows_events import NULL
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


from .models import Booking, Checkin
import datetime


def index(request):
    if "lodge" not in request.session:
        request.session["lodge"] = []
    return render(request, "lodge/index.html", {
        
        "bookings": Booking.objects.all(),
        "lodge": request.session["lodge"]   
    })

def checkin(request):
    now = datetime.datetime.now()
    return render(request, "lodge/checkin.html", {
        #"checkins": Checkin.objects.filter(checkin_date__isnull=True),
        "checkins": Checkin.objects.all(),
        "bookings": Booking.objects.filter(first_date=now),   
       
    })




def home(request):
    return render(request, "lodge/home.html")

def about(request):
    return render(request, "lodge/about.html")

def contact(request):
    return render(request, "lodge/contact.html")