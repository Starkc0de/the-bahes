from django.forms import ModelForm
from .models import PostService, Febric_Product, Thread_Product, Bottun_Product, Zipper_Product

class PostServiceForm(ModelForm):

    class Meta:
        model = PostService
        fields = '__all__'
    
class Post_Product_Form(ModelForm):

    class Meta:
        model = Febric_Product
        fields = '__all__'
    
class Thread_Product_Form(ModelForm):

    class Meta:
        model = Thread_Product
        fields = '__all__'
    
class Button_Product_Form(ModelForm):

    class Meta:
        model = Bottun_Product
        fields = '__all__'
    
    
class Zipper_Product_Form(ModelForm):

    class Meta:
        model = Zipper_Product
        fields = '__all__'
    
