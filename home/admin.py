from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *

# Register your models here.

class WorkAdmin(ModelAdmin):
    list_display = ["work", "Title_work", "discription_work", "image_work", "image_work_line",]

admin.site.register(How_Work,WorkAdmin)

class HomeAdmin(ModelAdmin):
    list_display = ["homelogo"]

admin.site.register(home_background,HomeAdmin)

class SuppliersAdmin(ModelAdmin):
    list_display = ["findSupplierlogo"]

admin.site.register(findSupplier_background,SuppliersAdmin)

class ProductAdmin(ModelAdmin):
    list_display = ["findproductlogo"]

admin.site.register(findproduct_background,ProductAdmin)

class ServiceAdmin(ModelAdmin):

    list_display = ["findservicelogo"]

admin.site.register(findservice_background,ServiceAdmin)

class RagisterAdmin(ModelAdmin):

    list_display = ["ragisterlogo", "aboutlogo", "contactlogo"]

admin.site.register(ragister_background,RagisterAdmin)