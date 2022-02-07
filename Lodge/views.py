from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.db import connection


from .models import Booking_rooms, Bookings, Checkin, Rooms
import datetime

# Create your views here.
def index(request):
    return render(request, "lodge/index.html", {
        "rooms": Rooms.objects.all(),
        "bookings": Bookings.objects.all()
    })


def checkin(request):
    now = datetime.datetime.now()

    with connection.cursor() as cursor:
        cursor.execute("'SELECT br.id, c.first_name, c.last_name, r.room_number FROM lodge_customers c JOIN lodge_bookings b ON c.id = b.customer_id_id JOIN lodge_booking_rooms br ON b.id = br.booking_id_id JOIN lodge_rooms r ON r.id = br.room_id_id LEFT JOIN lodge_checkin ch ON ch.booking_room_id_id = b.id WHERE ch.checkin_date IS NULL AND b.first_date <= "+ now +" AND b.last_date > "+now)
        customers_to_checkin = cursor.fetchall()
    #    customers_to_checkin = cursor.dictfetchall()
        #customers_to_checkin = cursor.getdescription()

        Bookings.objects

    #cust_list ={}
    #for row in customers_to_checkin:
    #    cust_list = {"id":row[0]}
    #    cust_list = {"first_name":row[1]}
    #    cust_list = {"last_name":row[2]}
    #    cust_list = {"room_number":row[3]}
    return render(request, "lodge/checkin.html", {
        "bookings": customers_to_checkin
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
