from django.contrib import admin
from .models import Teams, ContactMsg
from django.utils.html import format_html

class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'. format(object.photo.url))
    thumbnail.short_description = 'Image'

    list_display=('id','thumbnail','first_name','last_name','designation','created_date')
    list_display_links = ('id','thumbnail','first_name',)
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)

admin.site.register(Teams,TeamsAdmin)


class ContactMsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','timestamp')
    list_display_links = ('name', 'email', 'subject','timestamp')
    search_fields = ('name', 'email', 'subject','timestamp')

admin.site.register(ContactMsg, ContactMsgAdmin)
