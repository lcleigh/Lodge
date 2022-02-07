from asyncio.windows_events import NULL
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


from .models import Checkin, Customer
import datetime


# Create your views here.
def index(request): 
    return render(request, "lodge/index.html", {
        "checkins": Checkin.objects.all()
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
 

def home(request):
    return render(request, "lodge/home.html")

def about(request):
    return render(request, "lodge/about.html")

def contact(request):
    return render(request, "lodge/contact.html")