from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect('home')

def register(request):
        return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')