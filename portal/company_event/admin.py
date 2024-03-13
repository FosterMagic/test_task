from django.contrib import admin

from .models import Company, Event

# Register your models here.
admin.site.register(Company)
admin.site.register(Event)

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



