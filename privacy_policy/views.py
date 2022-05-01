from django.shortcuts import render
from django.views import generic
from .models import Privacy,Faqs
# Create your views here.

class PrivacyPageView(generic.TemplateView):
    template_name = "privacy_policy/privacy.html"

    def get(self, request, *args, **kwargs):
        privacy_policy = Privacy.objects.all()       

        return render(request, self.template_name, { 'privacy_policy': privacy_policy})   


class FaqPageView(generic.TemplateView):
    template_name = "privacy_policy/faq.html"

    def get(self, request, *args, **kwargs):
        faqs_policy = Faqs.objects.all()       

        return render(request, self.template_name, { 'faqs_policy': faqs_policy})

