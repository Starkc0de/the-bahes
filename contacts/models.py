from django.db import models

# Create your models here.

class ContactUs(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)

class ContactUs_Add(models.Model):
    address = models.CharField(max_length=50, null=True, blank=True)
    email_add = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.address)
