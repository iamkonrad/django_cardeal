from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from .choices import Year_Choices, Features_Choices, Doors_Choices



class Car(models.Model):
    car_name = models.CharField(max_length=500)
    country= CountryField(blank_label='(select a country)')
    province = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    production_year = models.IntegerField(('year'),choices=Year_Choices)
    condition = models.CharField(max_length=200)
    price = models.IntegerField()
    description = RichTextField()
    car_photo= models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    features = models.CharField(choices=Features_Choices, max_length=200)
    body_style = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    interior = models.CharField(max_length=200)
    mileage = models.IntegerField()
    doors = models.CharField(choices=Doors_Choices,max_length=20)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=200)
    number_of_owners = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
