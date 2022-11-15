from django.shortcuts import render, redirect
from fbvApp import models
from fbvApp import forms

# Create your views here.

def getStudents(request):
    student = models.Student.objects.all()
    return render(request, 'fbvApp/index.html', {'students':student})

def createStudent(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render( request, 'fbvApp/create.html', {'form': form})


def updateStudent(request,id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm( instance=student)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=student)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render (request, 'fbvApp/update.html', {'form': form})

def deleteStudent(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return redirect ('/')
