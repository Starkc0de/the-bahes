from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('', views.SupplierPageView.as_view(), name='supplier_page'),
    path('supplier_detail/<int:pk>/', views.SupplierDetailView.as_view(), name='detail_page'),

]
