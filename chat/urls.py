from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('<str:room_name>/', views.room.as_view(), name='room'),
    
]