from django.db import models

# Create your models here.

# --------------------------------about model----------------------------------

class About(models.Model):
    tittle = models.CharField(max_length=25, null=True, blank=True)
    sub_tittle = models.TextField(null=True, blank=True)
    about_disc = models.TextField(null=True, blank=True)
    about_image = models.ImageField(upload_to='About_data', null=True, blank=True)

    def __str__(self):
        return self.tittle