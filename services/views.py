from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from dashboard.models import PostService 
from services.models import ServiceTittle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.

class ServicePageView(generic.TemplateView):
    template_name = "services/services.html"

    def get(self,request):
        tittle =ServiceTittle.objects.all()
        service = PostService.objects.all()
        service_back = "service"

        p = Paginator(service, 4)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        return render(request, self.template_name,{'page_obj': page_obj, 'service': service, 'tittle': tittle, 'service_back':service_back})   
    

class ServiceDetailView(generic.DetailView):
    template_name = "services/servicesdetail.html"


