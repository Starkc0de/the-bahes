from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('', views.PrivacyPageView.as_view(), name='privacy_page'),
    path('faq', views.FaqPageView.as_view(), name='faq_page'),
]
