from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import EmailNewsletter


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You have been logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, ' Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    if request.method =='POST':
        auth.logout(request)
    messages.success(request,"You are now logged out.")
    return redirect('login')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists:
                    messages.error(request, 'Email already exists in the db')
                    return redirect ('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request,user)
                    messages.success(request,'Your account has been created. You are now logged-in')
                    return redirect('dashboard')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

@login_required(login_url = 'login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')



def subscribe(request):
    if request.method =="POST" and request.POST.get('EmailNewsletter'):
        email=request.POST.get('EmailNewsletter')
        exists=EmailNewsletter.objects.filter(email=email).exists()

        if not exists:
            EmailNewsletter.objects.create(email=email)
            messages.success(request, 'Your email has been added to our database.')
        else:
            messages.info(request,'This email has already been added.')

        referrer = request.META.get('HTTP_REFERER', reverse('home'))
        return redirect(f'{referrer}#newsletter-section')


    return redirect(reverse('home'))
