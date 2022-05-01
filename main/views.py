from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.views import generic
from dashboard.models import PostService 
from django import template
from django.template.defaulttags import register
from django.template.loader import render_to_string

# Create your views here.

class ServicePageView(generic.TemplateView):
    template_name = "main/base.template.html"

    def get(self,request,):
        service = PostService.objects.all()[:5]
        return render(request, "main/base.template.html", {"service":service })
