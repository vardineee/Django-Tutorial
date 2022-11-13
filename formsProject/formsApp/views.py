from django.shortcuts import render
from . import forms

# Create your views here.
def userLogin(request):
    form = forms.UserLoginForm()
    if request.method == "POST":
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['userName'])
    return render(request, 'formsApp/login.html', {'form':form})
