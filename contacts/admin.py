from django.contrib import admin
from .models import ContactUs, ContactUs_Add
from django.contrib.admin.options import ModelAdmin
# Register your models here.

# --------------------------------contactus admin----------------------------------

class ContactUsAdmin(ModelAdmin):
    list_display = ["first_name", "email", "message"]

admin.site.register(ContactUs,ContactUsAdmin)

# --------------------------------contact add admin----------------------------------

class ContactUsAddAdmin(ModelAdmin):
    list_display = ["address", "email_add", "phone"]

admin.site.register(ContactUs_Add,ContactUsAddAdmin)

