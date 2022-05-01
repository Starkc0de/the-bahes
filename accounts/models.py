from datetime import datetime
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


# Create your models here.

# --------------------------------Ragister model----------------------------------

class Ragister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country  = CountryField(blank=True)
    number = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_img', blank=True)
    Profile_date = models.DateTimeField(default=datetime.now, blank=True ,null=True)
    
    def __str__(self):
        return str(self.user)

