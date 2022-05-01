from itertools import chain
from django.shortcuts import redirect, render,get_object_or_404
from django.views import generic
from .models import SuppliersTittle
from dashboard .models import Thread_Product,Febric_Product
from dashboard .models import PostService
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class SupplierPageView(generic.TemplateView):
    template_name = "suppliers/suppliers.html"

    def get(self,request, **kwargs):
        context = super().get_context_data(**kwargs)
        suppliers = PostService.objects.all()
        thread = Thread_Product.objects.all()
        febric = Febric_Product.objects.all()
        result_list = list(chain(febric, thread))
        serviceSide = PostService.objects.all()[:4]
        tittle_service = SuppliersTittle.objects.all()
        supplier_back = "supplier" 

        p = Paginator(suppliers, 6)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        context = {'page_obj': page_obj, 'suppliers': suppliers,'result_list': result_list,  'serviceSide': serviceSide,  'tittle_service': tittle_service, 'supplier_back':supplier_back}

        return render(request, "suppliers/suppliers.html", context)     

class SupplierDetailView(generic.DetailView):
    template_name = "suppliers/supplier_detail.html" 
    model = PostService
                 
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post'] = PostService.objects.filter(id=self.kwargs['pk']) 
        context['febric'] = Febric_Product.objects.all()

        return context
    
