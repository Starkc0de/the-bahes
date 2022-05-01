from django.conf import settings
from django.shortcuts import render
from django.views import generic
from dashboard.models import PostService
from dashboard.models import Febric_Product, Thread_Product
from abouts.models import About
from .models import How_Work
from django.template.defaulttags import register
from .models import *

# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = PostService.objects.all()[:5]
        context['febric'] = Febric_Product.objects.all()[:6]
        context['thread'] = Thread_Product.objects.all()[:3]
        context['abouts'] = About.objects.all()
        context['How_Work'] = How_Work.objects.all()
        context ['service_count'] = PostService.objects.count()
        context['thread_count'] = Febric_Product.objects.count()
        context['homeback'] = "Home"                                           

        return context

@register.filter(name='background_img')
def background_img(demo):
    # background_img = settings.BASE_URL+"static/images/banner.png"
    if 'Home' == demo:
        if home_background.objects.all().exists():
            get_data = home_background.objects.all().first()
            if get_data.homelogo:
                background_img = get_data.homelogo.url
    elif 'supplier' == demo:
        if findSupplier_background.objects.all().exists():
            get_data = findSupplier_background.objects.all().first()
            if get_data.findSupplierlogo:
                background_img = get_data.findSupplierlogo.url
    elif 'product' == demo:
        if findproduct_background.objects.all().exists():
            get_data = findproduct_background.objects.all().first()
            if get_data.findproductlogo:
                background_img = get_data.findproductlogo.url
    elif 'service' == demo:
        if findservice_background.objects.all().exists():
            get_data = findservice_background.objects.all().first()
            if get_data.findservicelogo:
                background_img = get_data.findservicelogo.url
    elif 'ragister' == demo:
        if ragister_background.objects.all().exists():
            get_data = ragister_background.objects.all().first()
            if get_data.ragisterlogo:
                background_img = get_data.ragisterlogo.url
    elif 'abouts' == demo:
        if ragister_background.objects.all().exists():
            get_data = ragister_background.objects.all().first()
            if get_data.aboutlogo:
                background_img = get_data.aboutlogo.url
    elif 'contact' == demo:
        if ragister_background.objects.all().exists():
            get_data = ragister_background.objects.all().first()
            if get_data.contactlogo:
                background_img = get_data.contactlogo.url


    return str(background_img)