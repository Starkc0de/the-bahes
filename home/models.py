from django.db import models


# Create your models here.

# --------------------------------HOW IT WORKS---------------------------------- 

class How_Work(models.Model):
    work = models.CharField(max_length=50, null=True, blank=True)
    Title_work = models.CharField(max_length=50, null=True, blank=True,)
    discription_work = models.TextField(blank=True, null=True,)
    image_work = models.ImageField(upload_to='Home_work', null=True, blank=True)
    image_work_line = models.ImageField(upload_to='Home_work', null=True, blank=True)

    def __str__(self):
        return str(self.Title_work)

    class Meta:
        verbose_name_plural = "How_IT_Work"  # display table name for admin
        db_table = 'Howitwork' 


class home_background(models.Model):
    homelogo = models.ImageField(upload_to='home_logo', null=True, blank=True)

class findSupplier_background(models.Model):
    findSupplierlogo = models.ImageField(upload_to='supplier_logo', null=True, blank=True)    

class findproduct_background(models.Model):
    findproductlogo = models.ImageField(upload_to='product_logo', null=True, blank=True)    

class findservice_background(models.Model):
    findservicelogo = models.ImageField(upload_to='service_logo', null=True, blank=True)    

class ragister_background(models.Model):
    ragisterlogo = models.ImageField(upload_to='ragister_logo', null=True, blank=True)    
    aboutlogo = models.ImageField(upload_to='about_logo', null=True, blank=True)    
    contactlogo = models.ImageField(upload_to='contact_logo', null=True, blank=True)    

