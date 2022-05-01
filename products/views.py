from itertools import chain
from urllib import request
from django.shortcuts import render
from django.views import generic
from .models import ProductTittle
from dashboard.models import Febric_Product, Thread_Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaulttags import register
from django.template.loader import render_to_string
from dashboard.models import PostService 

# Create your views here.

class ProductPageView(generic.TemplateView):
    template_name = "products/product.html"
    model = ProductTittle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = ProductTittle.objects.all()
        febric = Febric_Product.objects.all()
        order_febric1 = Febric_Product.objects.filter(Fabric_Type='Fabric_Type').order_by('Fabric_Type')
        order_febric2 = Febric_Product.objects.order_by('Fabric_Price')
        order_febric3 = Febric_Product.objects.order_by('Tailor_Specialization')
        Thread = Thread_Product.objects.all()
        result_list = list(chain(febric, Thread))
        product_back = "product" 

        p = Paginator(febric, 6)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        context = {'page_obj': page_obj, 'result_list': result_list, 'title':title, 'order_febric1': order_febric1, 'order_febric2': order_febric2, 'order_febric3':order_febric3, 'product_back':product_back}

        return context    


class ProductDetailPageView(generic.DetailView):
    template_name = "products/product_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.kwargs['type'] == "Febric_Product": 
            context['instance'] = Febric_Product.objects.filter(id=self.kwargs['pk']) 
        if self.kwargs['type'] == "Thread_Product":
            context['instance'] = Thread_Product.objects.filter(id=self.kwargs['pk']) 

        return context
    
    def get_queryset(self ):
        if self.kwargs['type'] == "Thread_Product":
            query = Thread_Product.objects.filter(id=self.kwargs['pk'])
        if self.kwargs['type'] == "Febric_Product": 
            query = Febric_Product.objects.filter(id=self.kwargs['pk']) 
        return query



@register.filter(name='get_footer_services')
def get_footer_services(services):
        get_data = PostService.objects.all().values_list("Tailor_Specialization",flat=True) [:4]
        return render_to_string("products/footer.html", {"get_data": get_data})
 