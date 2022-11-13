from django.shortcuts import render
from modelForm import models
from modelForm import forms

# Create your views here.
def index(request):
    return render(request, 'modelFormApp/index.html')


def listProjects(request):
    projectslist = models.Project.objects.all()
    return render(request,'modelFormApp/listprojects.html', {'projects': projectslist})


def addProject(request):
    form = forms.ProjectForm()
    if request.method == "POST":
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render (request, 'modelFormApp/addProject.html', {'form': form})
