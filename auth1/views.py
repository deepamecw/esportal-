from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.


def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,' Account was created for ' + user)
            return redirect('login')
   
    context = {'form':form}
    return render(request,'auth/register.html',context)

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password =password )
        if username is not None:
            login(request, user) 
            return redirect('home')
        else:
           message= messages.info(request,"username or password is incorrect")
           return render(request,'auth/login.html')
            
    form = CreateUserForm()                		       
    context = {'form':form}
   
    return render(request,'auth/login.html',context)

def logoutpage(request):
    logout(request)
    message=messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required(login_url = 'login')
def home(request):
    date = datetime.date.today()
    return render(request,'auth/home.html',{'date':date})  