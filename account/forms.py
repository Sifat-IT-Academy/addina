from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    password = forms.CharField(max_length=15)
    username = forms.CharField(max_length=15)


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email','birth_date','phone_number', 'image')


