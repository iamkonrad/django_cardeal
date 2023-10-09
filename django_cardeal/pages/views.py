from django.contrib.auth.models import User
from django.shortcuts import render

from cars.models import Car
from .models import Teams


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
    return render(request,'pages/contact.html')
