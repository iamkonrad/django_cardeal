from django.contrib import admin
from .models import EmailNewsletter

# Register your models here.



class EmailNewsLetterAdmin(admin.ModelAdmin):
    list_display=('email','created_at','updated_at')


admin.site.register(EmailNewsletter, EmailNewsLetterAdmin)
