from django.contrib import admin
from .models import ProductTittle
from django.contrib.admin.options import ModelAdmin


# --------------------------------products admin----------------------------------

class ProducttittleAdmin(ModelAdmin):
    list_display = ["product_tittle",]

admin.site.register(ProductTittle,ProducttittleAdmin)