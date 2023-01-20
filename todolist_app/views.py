from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from todolist_app.models import Tasklist,request_from_contact,CustomUser,request_call
from todolist_app.forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from todolist_app.form2 import resultForm  
from django.contrib.auth.models import User

# Create your views here. 

@login_required
def todolist(request):    
    if request.method=="POST":
       form=Taskform(request.POST or None)
       if form.is_valid():
            instance= form.save(commit=False)
            instance.manage=request.user
            instance.save()
       messages.success(request,('the new investment has done successfully'))      
       return redirect('todolist')
    else:    
        users = CustomUser.objects.filter(username__exact=request.user).values
        form=Taskform(request.POST or None)
        all_task=Tasklist.objects.filter(manage=request.user)
        s=0
        for i in all_task:
            s=s+i.amount
        paginator = Paginator(all_task,5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)   
        return render(request,'todolist.html',{'myform':form,'all_task':all_task,'mydata':users,'total':s})
        
@login_required
def delete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,('you are not allowed to delete,Access denied '))
    return redirect('todolist') 

@login_required
def edit_task(request,task_id):
    if request.method=="POST":
       task = Tasklist.objects.get(pk=task_id)
       form=Taskform(request.POST or None,instance=task)
       if form.is_valid():
            form.save()
       messages.success(request,('the task is edited'))
       return redirect('todolist')    
    else:    
        single_obj=Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html',{'single_obj':single_obj})

def index(request):
    if request.user.is_authenticated:
        return render(request,"home1.html")
    else:
        return render(request,"home.html")


def about(request):
    if request.user.is_authenticated:
        return render(request,"about1.html")
    else:
        return render(request,"about.html")
    
def contact(request):
    if request.user.is_authenticated:
        return render(request,"contact1.html")
    else:
        return render(request,"contact.html")

@login_required
def complete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,('Access denied to you '))
    return redirect('todolist') 

@login_required
def pending_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist') 


@login_required 
def test1(request):  
    form = resultForm(request.POST or None)
    if request.method == 'POST':
        if request.POST['enterid']:
             task=Tasklist.objects.filter(pk=request.POST['enterid']).values
             context = {
              'mydata':task,'form':form,
             }          
        return render(request,'test1.html',context) 
    else:
        form = resultForm()  
        return render(request,'test1.html',{'form':form})  
    
def get_request_contact(request):   
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
                info=request_from_contact()
                info.name= request.POST.get('name')
                info.email= request.POST.get('email')
                info.message = request.POST.get('message')
                info.save()
                messages.success(request,('Your request is sent'))
                return render(request,'contact.html') 
            else:
                return render(request,'contact.html',context={})

        else:
            return render(request,'contact.html')


def APART(request):
    if request.user.is_authenticated:
        return render(request,"APART1.html")
    else:
        return render(request,"APART.html")
def careers(request):
    if request.user.is_authenticated:
        return render(request,"careers1.html")
    else:
        return render(request,"careers.html")

def request_call_details(request):
        if request.method=="POST":
            info=request_call()
            info.MobileNo = request.POST['MobileNo']
            info.ChooseDate = request.POST['ChooseDate']
            info.save()
            if request.user.is_authenticated:
                return render(request,'home1.html',context={'data':'Details submitted'})                
            else:
                return render(request,'home.html',context={'data':'Details submitted'})                
        else:
            return render(request,'home.html')
        
    