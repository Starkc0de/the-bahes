from django.contrib import admin
from .models import ServiceTittle
from django.contrib.admin.options import ModelAdmin

# Register your models here.

# --------------------------------service side admin----------------------------------

class ServiceTitileAdmin(ModelAdmin):
    list_display = ["service_tittle"]

admin.site.register(ServiceTittle,ServiceTitileAdmin)