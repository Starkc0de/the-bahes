from django.urls import path
from . import views 


urlpatterns = [

    path('', views.ServicePageView.as_view(), name='service_page'),
    

]
