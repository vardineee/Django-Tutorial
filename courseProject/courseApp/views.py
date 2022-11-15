from django.shortcuts import render, redirect
from courseApp import models
from courseApp import forms
# Create your views here.
def gettCourses(request):
    course = models.Course.objects.all()
    print(course)
    return render (request, 'courseApp/index.html', {'courses':course})


def createCourse(request):
    form = forms.CourseForm()
    if request.method == "POST":
        print(request.method)
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    return render (request, 'courseApp/create.html', {'form':form})


def updatCourse(request,id):
    course = models.Course.objects.get(id=id)
    form = forms.CourseForm(instance=course)
    if request.method == "POST":
        form = forms.CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render (request, 'courseApp/update.html', {'form':form})


def deleteCourse(request, id):
    course = models.Course.objects.get(id=id)
    course.delete()
    return redirect( '/')
