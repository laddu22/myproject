from django import forms
from todolist_app.models import Tasklist,CustomUser
from django.db import models





class Taskform(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields= ['task','amount','Date'] 
        widgets = {
            'Date':  forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}) 
        }
