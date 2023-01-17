from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from todolist_app.models import Tasklist,request_from_contact,CustomUser
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
        paginator = Paginator(all_task,5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)       
        return render(request,'todolist.html',{'myform':form,'all_task':all_task,'mydata':users})



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
    context = {
        'index_text':"welcome to Index Page"
    }
    return render(request,'home.html',context)


def about(request):
    context= {
        'about_text':"welcome aboutus page"
    }
    return render(request,'about.html',context)
def contact(request):
    context= {
        'contact_text':"welcome to contactus page"
    }
    return render(request,'contact.html',context)

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

def test(request):
    if request.method=='POST':   
        if request.POST['id'] is str:
            context = {
                        'mydata':'ENTER NUMBER'
            }
            return render(request,'test.html',context)
        else:
            task=Tasklist.objects.filter(pk=request.POST['id']).values
            context = {
                           'mydata':task
            }
            return render(request,'test.html',context)
    else:
        return render(request,'test.html',{})

@login_required 
def test1(request):  
    form = resultForm(request.POST or None)
    if request.method == 'POST':
        if request.POST['enterid']:
             task=Tasklist.objects.filter(pk=request.POST['enterid']).values
             print(request.user)
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
            return render(request,'contact.html')

