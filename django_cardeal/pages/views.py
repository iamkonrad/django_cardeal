from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from cars.models import Car
from .models import Teams,ContactMsg
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    teams = Teams.objects.all()
    featured_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    country_search=Car.objects.values_list('country',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('production_year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()
    doors_search=Car.objects.values_list('doors',flat=True).distinct()

    car_count = Car.objects.count()
    user_count = User.objects.count()


    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'country_search': country_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,
        'doors_search':doors_search,
        'car_count': car_count,
        'user_count': user_count,
    }
    return render (request,'pages/home.html',data)

def about(request):
    teams = Teams.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/about.html', data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    name = ''
    email = ''
    subject = ''
    phone = ''
    message = ''

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        contact_message = ContactMsg(
            name=name,
            email=email,
            subject=subject,
            phone=phone,
            message=message
        )
        contact_message.save()

#        email_subject = 'CarDeal message: ' + subject
#        msg_content = f'Name: {name}. Email: {email}. Phone_No: {phone}. Message: {message}'

#        admin_info = User.objects.get(is_superuser=True)
#        admin_email = admin_info.email
#        send_mail(
#            email_subject,
#            msg_content,
#            'yofdvcvcSail@someemailaddress93j4.com',
#            [admin_email],
#            fail_silently=False,
#        )

        messages.success(request, 'Thank you for reaching out to us. We will get back to you shortly.')

    return render(request, 'pages/contact.html')
