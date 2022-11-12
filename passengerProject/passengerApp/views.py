from django.shortcuts import render
from passengerApp import  models


# Create your views here.

def passengerdata(request):
    passenger = models.Passenger.objects.all()
    myDict = {"passengers": passenger}
    return render( request, 'passengerapp/info.html', myDict)
