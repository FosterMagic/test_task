from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Company, Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'company', 'get_html_photo', 'date')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('title', 'description')

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'address', 'postcode')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('title', 'description')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Event, EventAdmin)


# @admin.register(Company)
# class AdminCompany(admin.ModelAdmin):
#     fields = ['title', 'description', 'address', 'postcode']
#     save_on_top = True
#
#
# @admin.register(Event)
# class AdminEvent(admin.ModelAdmin):
#     fields = ['title', 'description', 'image']
#     save_on_top = True



