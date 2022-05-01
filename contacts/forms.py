from django import forms
from .models import ContactUs


class contact_us_Form(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['first_name', 'email', 'message' ]
