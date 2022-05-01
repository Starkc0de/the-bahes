from django.db import models

# Create your models here.

# --------------------------------service tittle model----------------------------------

class ServiceTittle(models.Model):
    service_tittle = models.CharField(max_length=25, null=True, blank=True)        
