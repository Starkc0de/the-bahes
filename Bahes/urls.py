"""Bahes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('about/', include(('abouts.urls', 'about'), namespace='about')),
    path('contact/', include(('contacts.urls', 'contact'), namespace='contact')),
    path('accounts/', include(('accounts.urls', 'account'), namespace='account')),
    path('products/', include(('products.urls', 'product'), namespace='product')),
    path('services/', include(('services.urls', 'service'), namespace='service')),
    path('suppliers/', include(('suppliers.urls', 'supplier'), namespace='supplier')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('privacy policy/', include(('privacy_policy.urls', 'privacy_policy'), namespace='privacy_policy')),
    # path('privacy chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
