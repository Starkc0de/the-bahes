from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('', views.HomePageView.as_view(), name='home_page')
]
