from django.shortcuts import render

from django.shortcuts import render, redirect
from .form import RegisterUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was error logging into this Account"))
            return redirect("login")
    
    else:
        return render(request, 'member/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logout, Try Login Again"))
    return redirect('home')

def register_user(request):
    if request.method =="POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful"))
            return redirect('home')
    else:
        form = RegisterUser()
    return render(request, 'member/register.html', {'form':form})

