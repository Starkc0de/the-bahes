from django.db import models

# --------------------------------Products tittle model----------------------------------

class ProductTittle(models.Model):
    product_tittle = models.CharField(max_length=25, null=True, blank=True)        

    def __str__(self):
        return self.product_tittle 