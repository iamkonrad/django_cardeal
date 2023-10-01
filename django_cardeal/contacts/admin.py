from django.contrib import admin
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','car_name','country','city','create_date')
    list_display_links=('id','first_name','last_name')
    search_fields=('first_name','last_name','email','car_title')
    list_per_page= 30

admin.site.register(Contact,ContactAdmin)