from django.contrib import admin
from .models import SuppliersTittle
from django.contrib.admin.options import ModelAdmin


# --------------------------------supplier admin----------------------------------

class SuppliersTittleAdmin(ModelAdmin):
    list_display = ["supplier_tittle"]

admin.site.register(SuppliersTittle, SuppliersTittleAdmin)