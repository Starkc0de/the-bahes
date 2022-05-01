from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('', views.ProductPageView.as_view(), name='product_page'),
    path('product_detail/<int:pk>/<str:type>/', views.ProductDetailPageView.as_view(), name='product_detail_page'),
    
]
