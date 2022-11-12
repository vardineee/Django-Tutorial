from django.shortcuts import render
from . import forms

# Create your views here.
def userRegistrationview(request):
    form = forms.UserRegistraionForm()
    if request.method == "POST":
        form = forms.UserRegistraionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['firstName'])
            print(form.cleaned_data['lastName'])
            print(form.cleaned_data['email'])

    return render (request, 'formsApp/userRegistration.html', {'form': form})
