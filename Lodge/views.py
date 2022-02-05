from asyncio.windows_events import NULL
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Booking, Checked_in_guest, Checkin, Room
import datetime


#tasks = ["foo", "bar","baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "lodge" not in request.session:
        request.session["lodge"] = []
    return render(request, "lodge/index.html", {
        "rooms": Room.objects.all(),
        "bookings": Booking.objects.all(),
        "checked_in_guests": Checked_in_guest.objects.all(),
        "lodge": request.session["lodge"]   
    })

def checkin(request):
    now = datetime.datetime.now()
    return render(request, "lodge/checkin.html", {
        "checkins": Checkin.objects.filter(checkin_date__isnull=True),
        "bookings": Booking.objects.filter(first_date=now),   
        "checked_in_guests": Checked_in_guest.objects.all()      
    })
    
def checked_in_guests(request):   
    return render(request, "lodge/checkin.html", {
        "checked_in_guests": Checked_in_guest.objects.all()     
    })


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["lodge"] += [task]
            return HttpResponseRedirect(reverse("lodge:index"))
        else:
            return render(request, "lodge/checkin.html", {
                "form": form
            })
    else:
        return render(request, "lodge/checkin.html", {
            "form": NewTaskForm()
        })