from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars':paged_cars,
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

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(model__iexact=city)

    if 'production_year' in request.GET:
        production_year = request.GET['production_year']
        if production_year:
            cars = cars.filter(model__iexact=production_year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(model__iexact=body_style)

    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)



    data = {
        'cars':cars,
    }

    return render (request,'cars/search.html',data)
