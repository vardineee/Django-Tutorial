from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from cbvApp import models
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(ListView):
    model = models.Student

    #default template_name is student_list.html
    #default context_object_name  is student_list

class StudentDetailView(DetailView):
    model = models.Student
    #default template_name is student_detail.html
    #default context_object_name is student


class StudentCreateView(CreateView):
    model = models.Student
    fields = ('firstName', 'lastName', 'testScore')


class StudentUpdateView(UpdateView):
    model = models.Student
    fields = ('testScore',)

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('students')
