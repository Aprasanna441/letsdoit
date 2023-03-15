from django.shortcuts import render

#Create your views here.
from ast import Not

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from listt.forms import TODOForm
from django.contrib.auth.decorators import login_required
from listt.models import todo
import datetime

from django.contrib.auth import authenticate , login as loginUser , logout

#Create your views here.
@login_required(login_url='login')
def welcome(request):
    user=request.user
    x=datetime.datetime.now()

   
        
    

    if  request.user.is_authenticated  :
        todoo=todo.objects.filter(user=user).order_by('priority')
        

       



       


    return render(request,"Templates/index.html",{'user':user,'todo':todoo,'todoform':TODOForm})

  


       


       
          
    
       

    
    
    return render(request,"Templates/index.html",{'todoform':TODOForm})

def login(request):
        user=request.user
        
    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                todoo=todo.objects.filter(user=user).order_by('priority')
                return render(request,'Templates/index.html',{'todo':todoo,'todoform':TODOForm})
        
        
    
   
        return render(request,"Templates/loginsignup.html",{'formauth':AuthenticationForm,'formsignup':UserCreationForm})

def signup(request):
    form=UserCreationForm(request.POST)
    
    if form.is_valid():
        user=form.save()

        if user is not None:
            loginUser(request , user)
            return redirect('welcome')
    return render(request,"Templates/loginsignup.html",{'formsignup':UserCreationForm,'formauth':AuthenticationForm})



def deletetask(request,id):
    task=todo.objects.get(pk=id)
    user=request.user
    count=todo.objects.all().filter(user=user)
  
         
    task.delete()
    return redirect('welcome')

def changestatus(request,id):
    task=todo.objects.get(pk=id)
    print(task.status)
    if task.status == 'C':
        task.status = 'P'
        task.save()
    else:
        task.status = 'C'
        task.save()

    return  redirect('welcome')   


def signout(req):
    logout(req)
    return redirect('signup')


def addtodo(request):
   if request.method=="POST":
     deadline_date=request.POST['deadline_date']
     deadline_time=request.POST['deadline_time']
     title=request.POST['title']
     status=request.POST['status']
     priority=request.POST['priority']
     user=request.user

     new_emp = todo(title=title,status=status,priority=priority,deadline_date=deadline_date,deadline_time=deadline_time,user=user)
     new_emp.save()
     todoo=todo.objects.filter(user=user).order_by('priority')
     
     

     return render(request,"Templates/index.html",{'todoform':TODOForm,'todo':todoo})


    
        


    
