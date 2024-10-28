from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
