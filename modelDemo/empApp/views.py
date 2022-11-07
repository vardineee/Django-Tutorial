from django.shortcuts import render
from empApp import models

# Create your views here.
def employeedata(request):
    employees = models.Employee.objects.all()
    # print(employees)
    empDict = {"employees":employees}
    return render (request,'empApp/emp.html', empDict)
