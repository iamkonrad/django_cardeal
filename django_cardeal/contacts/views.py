from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact



def enquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_interest = request.POST['customer_interest']
        country = request.POST['country']
        province = request.POST['province']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted = Contact.objects.filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an enquiry.')
                return redirect('/cars/'+car_id)


        contact = Contact(car_id=car_id, car_name=car_name, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_interest=customer_interest,country=country, province=province,
                          city=city,email=email, phone=phone, message=message)


        contact.save()
        messages.success(request, 'Your request has been submitted, we will contact you shortly.')
        return redirect ('/cars/'+car_id)
