from django.contrib import admin
from passengerApp.models import Passenger

# Register your models here.

class passengerAdmin(admin.ModelAdmin):
    list_display =['id','firstName', 'lastName', 'email', 'rewardPoints']

admin.site.register(Passenger,passengerAdmin)
