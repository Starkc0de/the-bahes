from itertools import chain
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from dashboard.forms import PostServiceForm, Post_Product_Form,Thread_Product_Form, Button_Product_Form, Zipper_Product_Form
from django.contrib import messages
from accounts.forms import Change_Password_Form, RegisterForm
from .models import PostService
from .models import Thread_Product, Febric_Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import Ragister
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

class CustomerPageView(generic.TemplateView):
    template_name = "dashboard/customer.html"


class ProfilePageView(LoginRequiredMixin,generic.TemplateView):
    template_name = "dashboard/profile.html"

    def get(self, request):
        if request.user.is_authenticated:
            profile = Ragister.objects.all()
            dashboard_back = "ragister" 

        return render(request, "dashboard/profile.html", {'profile': profile, 'dashboard_back':dashboard_back})         

    def post(self, request):
        if request.method == 'POST':
            form = Change_Password_Form(user=request.user, data=request.POST)
            if form.is_valid():
                print(form)
                user = form.save()
                print(user)
                print("=================")
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return render(request, "dashboard/profile.html")
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = Change_Password_Form(request.user)
        return render(request, "dashboard/profile.html", {'form': form}) 


# ************************************************ Start PostService  *******************************************************


class PostServiceView(generic.TemplateView):
    template_name = "dashboard/postservices.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = PostService.objects.all()
        profile = Ragister.objects.all()
        context = {'service': service, 'profile': profile}
        return context  

    def post(self, request,):
        if request.method == 'POST':
            if request.user.is_authenticated:
                form = PostServiceForm(request.POST, request.FILES,)
                if form.is_valid():
                    form.save()                
                    print("84516216351dadefef")
                    messages.success(request, f'Your service has been added ! You are now checkout')        
                    return render(request, "dashboard/postservices.html")
            else:
                form = PostServiceForm()
                messages.error(
                    request, f'Your account has not created ! You fill the right information')
            return render(request,  "dashboard/postservices.html", {'form': form})

class EditServiceView(generic.TemplateView):
    template_name = "dashboard/editservice.html"
    form = PostServiceForm

    def get(self, request, id, *args, **callback_kwargs):
        instance = get_object_or_404(PostService, id=id)
        specialization = PostService.objects.all().values_list('Tailor_Specialization', flat=True)[:1]
        customer = PostService.objects.all().values_list('Targeted_Customer', flat=True)[:1]
        gender = PostService.objects.all().values_list('Tailor_Staff_Gender', flat=True)[:1]
        Address = PostService.objects.all().values_list('Full_Address', flat=True)[:1]
        service = PostService.objects.all()
        
        return render(request, "dashboard/editservice.html", {'instance':instance, 'service':service,'customer':customer,'gender':gender,  'specialization':specialization , 'Address':Address})

    def post(self, request, id, *args, **kwargs):
        service1 = get_object_or_404(PostService, id=id)    
        form = PostServiceForm(request.POST or None, instance=service1)
        if form.is_valid():
            form.save()
            return render(request, "dashboard/editservice.html", {'form':form})           
        context = {"form": form , "service1":service1}
        return render(request, "dashboard/editservice.html", context)

class ServiceDeleteView(generic.TemplateView):
    template_name = "dashboard/postservices.html"

    def post(self, request, id, *args, **kwargs):
        service = get_object_or_404(PostService, id=id)
        PostService.objects.filter(id=service.id).delete()
        return render(request, "dashboard/postservices.html")

# ************************************************ End PostService  *******************************************************
# ************************************************ Start Product  *******************************************************


class MyproductView(generic.TemplateView):
    template_name = "dashboard/myproduct.html"

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        Thread_products =Thread_Product.objects.all()
        Febric_product = Febric_Product.objects.all()
        profile = Ragister.objects.all()
        result_list = list(chain(Thread_products, Febric_product))

        p = Paginator(result_list, 5)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page(2)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        context = {'page_obj': page_obj, 'result_list': result_list, 'profile':profile}

        return render(request, "dashboard/myproduct.html", context) 
             
    def post(self, request,):
        form = Post_Product_Form(request.POST, request.FILES,)
        form1 = Thread_Product_Form(request.POST, request.FILES,)
        form2 = Button_Product_Form(request.POST, request.FILES,)
        form3 = Zipper_Product_Form(request.POST, request.FILES,)

        if request.method == 'POST' and 'htmlsubmitbutton1' in request.POST:
            if form.is_valid():
                print(form)
                form.save()
                print('1')
        if request.method == 'POST' and 'htmlsubmitbutton2' in request.POST:
            if form1.is_valid():
                print(form1)
                form1.save()
                print('2')        
        # if request.POST.get("htmlsubmitbutton3") != None:
        if request.method == 'POST' and 'htmlsubmitbutton3' in request.POST:
            if form2.is_valid():
                print(form2)
                form2.save()
                print('3')        
        if request.method == 'POST' and 'htmlsubmitbutton4' in request.POST:
            if form3.is_valid():
                print(form3)
                form3.save()
                print('4')        
                messages.success(request, f'Your service has been added ! You are now checkout')        
                return render(request, "dashboard/myproduct.html")
            else:
                form = Post_Product_Form()
                messages.error(
                    request, f'Your account has not created ! You fill the right information')
        context = {
        'form': form,
        'form1': form1,
        'form2': form2,
        'form3': form3,
    }            
        return render(request,  "dashboard/myproduct.html", context)   

class EditProductView(generic.TemplateView):
    template_name = "dashboard/editproduct.html"
    form = Post_Product_Form

    def get(self, request, id, *args, **callback_kwargs):
        instance = get_object_or_404(Febric_Product, id=id)
        product = Febric_Product.objects.all()
        
        return render(request, "dashboard/editproduct.html", {'instance':instance, 'product':product,})

    def post(self, request, id, *args, **kwargs):
        product_febric = get_object_or_404(Febric_Product, id=id)    
        form = Post_Product_Form(request.POST or None, instance=product_febric)
        if form.is_valid():
            form.save()
            return render(request, "dashboard/editproduct.html", {'form':form})           
        context = {"form": form , "service1":product_febric}
        return render(request, "dashboard/editproduct.html", context)

class ProductDeleteView(generic.TemplateView):
    template_name = "dashboard/myproduct.html"

    def post(self, request, id, *args, **kwargs):
        service = get_object_or_404(Febric_Product, id=id)
        Febric_Product.objects.filter(id=service.id).delete()
        return render(request, "dashboard/myproduct.html")        

# ************************************************ End Product  *******************************************************

class ChatView(generic.TemplateView):
    template_name = "dashboard/chat.html"

    def get(self, request):
        if request.user.is_authenticated:
            profile = Ragister.objects.all()

        return render(request, "dashboard/chat.html", {"profile":profile})   


class Supplier_1View(generic.TemplateView):
    template_name = "dashboard/supplier_1.html"


class SupplierView(generic.TemplateView):
    template_name = "dashboard/supplier.html"


class ServiceStatus(generic.TemplateView):
    template_name = 'services/my-services.html'

    def post(self, request, *args, **kwargs):

        serviceid = request.POST["serviceid"]
        servicestatus = request.POST["servicestatus"]

        if servicestatus == "True":
            status = False
        else:
            status = True
        if PostService.objects.filter(id=serviceid).exists():
            # service_instance = get_object_or_404(SupplierServices, id=serviceid)
            PostService.objects.filter(id=serviceid).update(status=status)
        return JsonResponse({'message': 'Status Changed successfully.'})








