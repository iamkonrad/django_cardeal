from django.db import models
from datetime import datetime
from django_countries.fields import CountryField



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_interest = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    country= CountryField(blank_label='(select a country)')
    province = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email



