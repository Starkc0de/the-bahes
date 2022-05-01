from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from colorfield.fields import ColorField
from django.contrib.auth.models import User


# Create your models here.
 
# --------------------------------Services model----------------------------------

GENDER_CHOICES =(
    ("Male", "Male"),
    ("Female", "Female"),
)

SERVICE_CHOICES =(
    ("CASUAL CLOTHES", "CASUAL CLOTHES"),
    ("WEDDING SERVICES", "WEDDING SERVICES"),
    ("SUIT RESIZING", "SUIT RESIZING"),
    ("DESHDASHA", "DESHDASHA"),
    ("GOWN DRESSES", "GOWN DRESSES"),
    ("CUSTOM ACCESSORIES", "CUSTOM ACCESSORIES"),
)

YES_CHOICES =(
    ("YES", "YES"),
    ("NO", "NO"),
)


class PostService(models.Model):
    Service_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Supplier_Name = models.CharField(max_length=25, null=True, blank=True)
    Business_Country_Location = CountryField(blank=True,null=True,)
    Tailor_Specialization = models.CharField(max_length=50, null=True, blank=True, choices = SERVICE_CHOICES)
    Experience = models.CharField(max_length=50, null=True, blank=True)
    Multinational_Shippping = models.CharField(max_length=25, null=True, blank=True, choices = YES_CHOICES , default='YES')
    Targeted_Customer = models.CharField(max_length=25, null=True, blank=True, choices = GENDER_CHOICES , default='Casual Clothes')
    Tailor_Staff_Gender = models.CharField(max_length=25, null=True, blank=True, choices = GENDER_CHOICES )
    Phone_Number = models.IntegerField(null=True, blank=True)
    Full_Address = models.TextField(null=True, blank=True)
    Check_Box = models.BooleanField()
    service_disc = models.TextField(null=True, blank=True)
    service_image = models.ImageField(upload_to='Service_data', blank=True)

    def __str__(self):
        return str(self.Supplier_Name)

# --------------------------------Febric model----------------------------------   

class Febric_Product(models.Model):
    type1 = models.CharField(max_length=50, default="Febric_Product", null=True, blank=True)
    Febric_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Country_Origin = CountryField(blank=True)
    Fabric_Type = models.CharField(max_length=50, null=True, blank=True)
    Tailor_Specialization = models.CharField(max_length=25, null=True, blank=True,)
    Fabric_Price = models.CharField(max_length=25, null=True, blank=True)
    Fabric_Available_Quantity = models.CharField(max_length=25, null=True, blank=True)
    Fabric_Season = models.CharField(max_length=25, null=True, blank=True )
    Other_Description = models.TextField(null=True, blank=True)
    Upload_Image = models.ImageField(upload_to='Post_Product', null=True, blank=True)
    Size_Width = models.IntegerField(null=True, blank=True)
    Check_Febric = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.Fabric_Type)

    class Meta:
        verbose_name_plural = "febric"  # display table name for admin
        db_table = 'ProductCategory'  
      

# --------------------------------Thread Product model----------------------------------   


class Thread_Product(models.Model):
    type2 = models.CharField(max_length=50, default="Thread_Product", null=True, blank=True)
    Thread_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Thread_Type = models.CharField(max_length=50, null=True, blank=True,)
    Thread_Price = models.CharField(max_length=50, null=True, blank=True)
    Thread_Available_Quantity = models.CharField(max_length=25, null=True, blank=True)
    Thread_Description = models.TextField(null=True, blank=True)
    Thread_Image = models.ImageField(upload_to='Post_Product', null=True, blank=True)

    def __str__(self):
        return str(self.Thread_Type)

    class Meta:
        verbose_name_plural = "thread"  # display table name for admin
        db_table = 'ThreadCategory'  

# --------------------------------Button Product model----------------------------------  

class Bottun_Product(models.Model):
    type3 = models.CharField(max_length=50, default="Bottun_Product", null=True, blank=True)
    Bottun_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Type_Of_Material = models.CharField(max_length=50, null=True, blank=True,)
    Origin = CountryField(blank=True)
    Size = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Color_Picker = ColorField(format='hexa')
    B_Description = models.TextField(null=True, blank=True)
    B_Upload_Image = models.ImageField(upload_to='Service_data', null=True, blank=True)
    B_Upload_Image_1 = models.ImageField(upload_to='Service_data', null=True, blank=True)

    def __str__(self):
        return str(self.Type_Of_Material)

    class Meta:
        verbose_name_plural = "bottum"  # display table name for admin
        db_table = 'bottumCategory'     

# --------------------------------Zipper Product model----------------------------------  

class Zipper_Product(models.Model):
    type4 = models.CharField(max_length=50, default="Zipper_Product", null=True, blank=True)
    Zipper_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Z_Type = models.CharField(max_length=50, null=True, blank=True,)
    Country_4 = CountryField(blank=True)
    Size_Zipper = models.CharField(max_length=25, null=True, blank=True)
    Z_Price = models.IntegerField(null=True, blank=True)
    Z_Color_Picker = models.CharField(max_length=50, null=True, blank=True,)
    Roller = models.CharField(max_length=25, null=True, blank=True)
    Z_Upload_Image = models.ImageField(upload_to='Service_data', null=True, blank=True)
    D_Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.Type)

    class Meta:
        verbose_name_plural = "zipper"  # display table name for admin
        db_table = 'zipperCategory'         








