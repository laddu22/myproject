from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todolist_app.models import CustomUser
from django.contrib.auth import get_user_model

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model  = CustomUser
        fields  = ['username','first_name','last_name','email','password1','password2']