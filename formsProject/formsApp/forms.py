from django import forms
from django.core import validators

class UserLoginForm(forms.Form):
    userName = forms.CharField(validators=[validators.MaxLengthValidator(15)])
    password = forms.CharField(validators=[validators.MinLengthValidator(8)])
