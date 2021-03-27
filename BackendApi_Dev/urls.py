"""BackendApi_Dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from restapp.views import *
from customerApp.views import *
from django.conf import settings
import django
from django.conf.urls.static import static
from django.contrib.auth import views 

urlpatterns = [
     path('accounts/', include('allauth.urls')),
    # path('<int:order_id>/smssend/',SendSms,name='sms'),
    path('signup',SignUp,name='signup'),
     path('accounts/login/',views.LoginView.as_view(template_name='account/login.html'),name='login'),
     path('logout/',views.LogoutView.as_view(),name='logout'),
     path('<int:item_id>/orderpage',OrderPage,name="orderpage"),
     path('<int:order_id>/checkout',ConfirmOrder,name="checkout"),
     path('order_detail/',OrderDetails,name="order_detail"),
    path('openid/',include('oidc_provider.urls',namespace='oidc_provider')),
    path('itemsapi/',ItemApiView.as_view(),name="itemsapi"),
    path('orderapi/',OrderApi.as_view(),name="orderapi"),
    path('customerapi/',CustomerApiView.as_view(),name="customer_api"),
    path('',ItemsPage,name='home'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
