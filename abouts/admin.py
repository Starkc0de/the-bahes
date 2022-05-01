from django.contrib import admin
from .models import About
from django.contrib.admin.options import ModelAdmin
# Register your models here.

# --------------------------------faq admin----------------------------------

class FaqsAdmin(ModelAdmin):
    list_display = ["tittle", "sub_tittle", "about_image"]

admin.site.register(About,FaqsAdmin)