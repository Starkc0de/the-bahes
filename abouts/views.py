from django.shortcuts import render
from django.views import generic
from .models import About
# Create your views here.

class AboutPageView(generic.TemplateView):
    template_name = "abouts/about.html"

    def get(self, request, *args, **kwargs):
        about_us = About.objects.all()
        about_back = "abouts"
        
        return render(request, self.template_name, { 'about_us': about_us, 'about_back':about_back})
