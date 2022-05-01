from distutils.command.upload import upload
from django.db import models

# Create your models here.

# --------------------------------Faq model----------------------------------

class Faqs(models.Model):
    tittle = models.CharField(max_length=25, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    questions = models.CharField(max_length=250, null=True, blank=True)
    answer = models.TextField( null=True, blank=True)
    faq_image = models.ImageField(upload_to='Faq_data', null=True, blank=True)

    def __str__(self):
        return self.tittle
# --------------------------------Privacy model----------------------------------

class Privacy(models.Model):
    tittle_privacy = models.CharField(max_length=25, null=True, blank=True)
    discription_privacy = models.TextField(null=True, blank=True)
    privacy_image = models.ImageField(upload_to='Privacy_data', null=True, blank=True)

    def __str__(self):
        return self.tittle_privacy