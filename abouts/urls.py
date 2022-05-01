from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('', views.AboutPageView.as_view(), name='about_page')
]
