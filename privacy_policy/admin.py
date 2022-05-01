from django.contrib import admin
from .models import Faqs,Privacy
from django.contrib.admin.options import ModelAdmin
# Register your models here.

# --------------------------------faq admin----------------------------------

class FaqsAdmin(ModelAdmin):
    list_display = ["tittle", "discription", "questions", "answer", "faq_image"]

admin.site.register(Faqs,FaqsAdmin)

# --------------------------------about admin----------------------------------

class PrivacyAdmin(ModelAdmin):
    list_display = ["tittle_privacy", "discription_privacy", "privacy_image"]

admin.site.register(Privacy,PrivacyAdmin)

