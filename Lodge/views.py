from asyncio.windows_events import NULL
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


from .models import Checkin, Customer, Checkout, Guest
import datetime


# Create your views here.
def index(request): 
    return render(request, "lodge/index.html", {
        "checkins": Checkin.objects.all(),
        "checkouts": Checkout.objects.all()
    })

def check(request): 
    return render(request, "lodge/check.html", {
        "checkins": Checkin.objects.all(),
        "checkouts": Checkout.objects.all()
    })


def checkin(request, checkin_id):
    try:
        checkin = Checkin.objects.get(id=checkin_id)
    except Checkin.DoesNotExist:
        raise Http404("checkin not found.")
    return render(request, "lodge/checkin.html", {
        "checkin": checkin,
        "customers": checkin.customers.all(),
        "non_customers": Customer.objects.exclude(checkins=checkin).all()
    })

def checkout(request, checkout_id):
    try:
        checkout = Checkout.objects.get(id=checkout_id)
    except Checkout.DoesNotExist:
        raise Http404("checkout not found.")
    return render(request, "lodge/checkout.html", {
        "checkout": checkout,
        "guests": checkout.guests.all(),
        "non_guests": Guest.objects.exclude(checkouts=checkout).all()
    })


#this is from CS50 airline example
def book(request, checkin_id):
    if request.method == "POST":
        try:
            customer = Customer.objects.get(pk=int(request.POST["customer"]))
            checkin = Checkin.objects.get(pk=checkin_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no customer chosen")
        except Checkin.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: customer does not exist")
        except Customer.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: booking does not exist")
        customer.checkins.add(checkin)
        return HttpResponseRedirect(reverse("checkin", args=(checkin_id,)))

def unbook(request, checkout_id):
    if request.method == "POST":
        try:
            guest = Guest.objects.get(pk=int(request.POST["guest"]))
            checkout = Checkout.objects.get(pk=checkout_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no customer chosen")
        except Checkout.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: customer does not exist")
        except Guest.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: booking does not exist")
        guest.checkouts.remove(checkout)
        return HttpResponseRedirect(reverse("checkout", args=(checkout_id,)))
 

def home(request):
    return render(request, "lodge/home.html")

def booking(request):
    return render(request, "lodge/booking.html")

def room(request):
    return render(request, "lodge/room.html")