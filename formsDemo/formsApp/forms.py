from django import forms
from django.core import validators

class UserRegistraionForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female', 'FEMALE')]
    firstName = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(8)])
    lastName = forms.CharField()
    email = forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER), required=False)
    password = forms.CharField(widget=forms.PasswordInput)


'''
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length should be 20 characters')

        inputEmail = user_cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('The email should contain @')



    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length should be 20 characters.')
        return inputFirstName

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('The email should contain @')
        return inputEmail
'''
