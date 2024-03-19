from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 40)
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']