from django import forms
from django.forms import CharField, ModelForm, PasswordInput
from .models import Ragister
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
                
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

  
class Change_Password_Form(PasswordChangeForm):

    class Meta:
        fields = ["old_password", "new_password1", "new_password2"]



class RegisterForm(ModelForm):

    class Meta:
        model = Ragister
        fields = ["country", "number", "profile_image", "Profile_date"]
    
class EditProfileForm(ModelForm):

    class Meta:
        model = User
        fields = (
                 'email',
                 'first_name',
                )
class ProfileForm(ModelForm):
    class Meta:
        model = Ragister
        fields = ('number', 'profile_image') #Note that we didn't mention user field here.