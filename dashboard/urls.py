from django.urls import path
from . import views


urlpatterns = [

    path('', views.CustomerPageView.as_view(), name='dashboard_page'),
    path('profile/', views.ProfilePageView.as_view(), name='profile_page'),
    path('my_product/', views.MyproductView.as_view(), name='my_product_page'),
    path('Edit_Product/<int:id>', views.EditProductView.as_view(), name="Product_edit"),
    path('del_product/<int:id>', views.ProductDeleteView.as_view(), name="delelte_product"),
    path('chat/', views.ChatView.as_view(), name='chat_page'),
    path('supplier_1/', views.Supplier_1View.as_view(), name='supplier_1_page'),
    path('supplier/', views.SupplierView.as_view(), name='supplier_page'),
    path('my_service/', views.PostServiceView.as_view(), name='my_service_page'),
    path('Edit_service/<int:id>', views.EditServiceView.as_view(), name="Service_edit"),
    path('del_service/<int:id>', views.ServiceDeleteView.as_view(), name="del_service1"),
    path('servicestatus', views.ServiceStatus.as_view(), name="ServiceStatus"),

]
