from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('', views.ContactPageView.as_view(), name='contact_page')
]
