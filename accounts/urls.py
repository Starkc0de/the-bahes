from django.urls import path
from . import views
# from home.views import HomePageView

urlpatterns = [

    path('registraion/', views.RegistraionPageView.as_view(), name='registration_page'),
    path('login', views.LoginPageView.as_view(), name='login_page'),
    path('logout/', views.LogoutPageView, name='logout_page'),
    path('forgot/', views.ForgotPageView.as_view(), name='forgot_page'),
    
]
