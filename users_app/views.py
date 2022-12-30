from django.shortcuts import render,redirect
from django.contrib import messages
from users_app.forms import CustomRegisterForm

def register(request):
    if request.method=="POST":
        registration_form = CustomRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,('New User account created'))
            return redirect('register')  
    else:
        registration_form = CustomRegisterForm()
    return render(request,'register.html',{'registration_form': registration_form })
