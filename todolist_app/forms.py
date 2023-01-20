from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from todolist_app.models import Tasklist,CustomUser
from django.db import models





class Taskform(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields= ['task','amount','Date'] 
        widgets = {
            'Date': widgets.DateInput(format = '%dd/%mm/%Y',attrs={'type': 'date'})
        }
        ordering = ['-Date']