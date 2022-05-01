from django.contrib import admin
from .models import PostService, Febric_Product , Thread_Product, Bottun_Product, Zipper_Product
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class PostServiceAdmin(ModelAdmin):
    list_display = ["Supplier_Name", "Business_Country_Location", "Tailor_Specialization","Targeted_Customer", "Tailor_Staff_Gender", "Phone_Number","Full_Address", "Check_Box", "service_disc", "Multinational_Shippping",  "service_disc", "Experience",]

admin.site.register(PostService,PostServiceAdmin)

# -----------------------------------------------------------------------------------

class Febric_Product_Admin(ModelAdmin):
    list_display = ["Country_Origin", "Fabric_Type", "Tailor_Specialization","Fabric_Price", "Fabric_Available_Quantity", "Fabric_Season","Other_Description", "Upload_Image", "Size_Width", "Check_Febric",]

admin.site.register(Febric_Product,Febric_Product_Admin)

# -----------------------------------------------------------------------------------

class Thread_Product_Admin(ModelAdmin):
    list_display = ["Thread_Type", "Thread_Price", "Thread_Available_Quantity","Thread_Description", "Thread_Image",]

admin.site.register(Thread_Product,Thread_Product_Admin)

# -----------------------------------------------------------------------------------

class Button_Product_Admin(ModelAdmin):
    list_display = ["Type_Of_Material", "Origin", "Size","B_Description", "B_Upload_Image", "B_Upload_Image_1", "Price", "Color_Picker", ]

admin.site.register(Bottun_Product,Button_Product_Admin)

# -----------------------------------------------------------------------------------

class Zipper_Product_Admin(ModelAdmin):
    list_display = ["Z_Type", "Country_4", "Size_Zipper","Z_Price", "Z_Color_Picker", "Roller", "Z_Upload_Image", "D_Description", ]

admin.site.register(Zipper_Product,Zipper_Product_Admin)