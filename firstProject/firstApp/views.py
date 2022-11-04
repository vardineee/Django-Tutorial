from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>Hello First DJango App!!</h1>")

def currentDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Curret dateime is </b>" + str(dt)
    return HttpResponse(s)
