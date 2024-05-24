from django.shortcuts import render, redirect       
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'Invalid credentials')
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html')  
# Create your views here.
