from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('production_year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()

    data = {
        'cars':paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)

    data = {
        'single_car':single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search (request):
    cars = Car.objects.order_by('-created_date')
    keyword=Car.objects.values_list('model',flat=True).distinct()
    model_search=Car.objects.values_list('model',flat=True).distinct()
    country_search=Car.objects.values_list('country',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('production_year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'country' in request.GET:
        country=request.GET['country']
        if country:
            cars=cars.filter(country__iexact=country)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'production_year' in request.GET:
        production_year = request.GET['production_year']
        if production_year:
            cars = cars.filter(production_year__exact=production_year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission=request.GET['transmission']
        if transmission:
            cars=cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)


    data = {
        'cars':cars,
        'keyword':keyword,
        'model_search': model_search,
        'country_search': country_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,

    }

    return render (request,'cars/search.html',data)
