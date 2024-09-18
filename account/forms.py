from .models import User
from django import forms

class LoginForm(forms.Form):
    password = forms.CharField(max_length=15)
    username = forms.CharField(max_length=15)

