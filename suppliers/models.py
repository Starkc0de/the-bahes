from django.db import models


# --------------------------------service tittle model----------------------------------

class SuppliersTittle(models.Model):
    supplier_tittle = models.CharField(max_length=25, null=True, blank=True)        

    def __str__(self):
        return self.supplier_tittle
