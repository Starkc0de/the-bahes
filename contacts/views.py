from django.shortcuts import get_object_or_404, render
from django.views import generic
from .forms import contact_us_Form
from .models import ContactUs_Add
# Create your views here.

class ContactPageView(generic.TemplateView):
    template_name = "contacts/contact.html"

    def get(self, request):
        contact_back = "contact"
        
        return render(request, self.template_name, {'contact_back':contact_back})

    def post(self,request):
        if request.method == 'POST':
            form = contact_us_Form(request.POST)
            if form.is_valid():
                form.save()  
                return render(request, "home/index.html")

        else:
            form = contact_us_Form()
        return render(request, "home/index.html")  

