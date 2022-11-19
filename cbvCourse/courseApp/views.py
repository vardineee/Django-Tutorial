from django.shortcuts import render
from django.views import generic
from courseApp import models
from django.urls import reverse_lazy

# Create your views here.

class CourseListView(generic.ListView):
    model = models.Course



class CourseDetailView(generic.DetailView):
    model = models.Course



class CourseCreateView(generic.CreateView):
    model = models.Course
    fields = ('name', 'description', 'instructor', 'rating')


class CourseUpdateView(generic.CreateView):
    model = models.Course
    fields = ('description', 'rating')


class CourseDeleteView(generic.DeleteView):
    model = models.Course
    success_url = reverse_lazy('courses')
