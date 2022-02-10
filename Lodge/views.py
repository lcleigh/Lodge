from tabnanny import check
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.contrib import messages
from django.utils.translation import get_language


from .models import Booking_rooms, Bookings, Checkin, Rooms
import datetime

# Create your views here.
def index(request):
    return render(request, "lodge/index.html", {
        "rooms": Rooms.objects.all(),
        "bookings": Bookings.objects.all()
    })


def checkin(request):

    now = str(datetime.datetime.now())
    now = "'{}'".format(now)

    with connection.cursor() as cursor:
        query = "SELECT br.id, c.first_name, c.last_name, r.room_number FROM lodge_customers c JOIN lodge_bookings b ON c.id = b.customer_id_id JOIN lodge_booking_rooms br ON b.id = br.booking_id_id JOIN lodge_rooms r ON r.id = br.room_id_id LEFT JOIN lodge_checkin ch ON ch.booking_room_id_id = br.id WHERE ch.checkin_date IS NULL AND b.first_date <= "+ now+" AND b.last_date > "+now 
        cursor.execute(query)
        customers_to_checkin = cursor.fetchall()

        query = "SELECT br.id, c.first_name, c.last_name, r.room_number FROM lodge_customers c JOIN lodge_bookings b ON c.id = b.customer_id_id JOIN lodge_booking_rooms br ON b.id = br.booking_id_id JOIN lodge_rooms r ON r.id = br.room_id_id LEFT JOIN lodge_checkin ch ON ch.booking_room_id_id = br.id LEFT JOIN lodge_checkout cho ON ch.booking_room_id_id = br.id WHERE ch.checkin_date IS NOT NULL AND b.last_date <="+now
        cursor.execute(query)
        customers_to_checkout = cursor.fetchall()

        checkin_list = list(customers_to_checkin)
        checkout_list = list(customers_to_checkout)

    return render(request, "lodge/checkin.html", {
        "tocheckin": checkin_list,
        "tocheckout": checkout_list
    })

def checked_in(request):
    if request.method == "POST":
        booking_check_id = request.POST["cust"]

        #write to the database
        with connection.cursor() as cursor:
            query = "INSERT INTO lodge_checkin (booking_room_id_id, checkin_date) VALUES ("+booking_check_id+", curdate())"
            cursor.execute(query)

            query = "SELECT c.first_name, c.last_name, r.room_number FROM lodge_customers c JOIN lodge_bookings b ON c.id = b.customer_id_id JOIN lodge_booking_rooms br ON b.id = br.booking_id_id JOIN lodge_rooms r ON r.id = br.room_id_id LEFT JOIN lodge_checkin ch ON ch.booking_room_id_id = br.id WHERE ch.booking_room_id_id ="+booking_check_id
            cursor.execute(query)
            checked_in = cursor.fetchall()

            checkedin_list = list(checked_in)
            
            messages.success(request, (str(checkedin_list[0][0])+" "+str(checkedin_list[0][1])+" is checked into room number "+str(checkedin_list[0][2])))
            return redirect("checkin")
            #return HttpResponseRedirect("lodge/checkin.html")

def checked_out(request):
    if request.method == "POST":
        booking_check_id = request.POST["cust"]

        #write to the database
        with connection.cursor() as cursor:
            query = "INSERT INTO lodge_checkout (booking_room_id_id, checkin_date) VALUES ("+booking_check_id+", curdate())"
            cursor.execute(query)

            query = "SELECT c.first_name, c.last_name, r.room_number FROM lodge_customers c JOIN lodge_bookings b ON c.id = b.customer_id_id JOIN lodge_booking_rooms br ON b.id = br.booking_id_id JOIN lodge_rooms r ON r.id = br.room_id_id LEFT JOIN lodge_checkout ch ON ch.booking_room_id_id = br.id WHERE ch.booking_room_id_id ="+booking_check_id
            cursor.execute(query)
            checked_out = cursor.fetchall()

            checkedout_list = list(checked_out)
            
            messages.success(request, (str(checkedout_list[0][0])+" "+str(checkedout_list[0][1])+" is checked out of room number "+str(checkedout_list[0][2])))
            return redirect("checkin")

def home(request):
    return render(request, "lodge/home.html")

def about(request):
    return render(request, "lodge/about.html")

def contact(request):
    return render(request, "lodge/contact.html")