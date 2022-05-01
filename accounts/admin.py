from django.contrib import admin
from .models import Ragister
from django.contrib.admin.options import ModelAdmin

# Register your models here.

# --------------------------------faq admin----------------------------------

class RagisterAdmin(ModelAdmin):
    list_display = ["user", "country", "number", "profile_image" ,"Profile_date"]

admin.site.register(Ragister,RagisterAdmin)