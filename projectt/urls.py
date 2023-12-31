"""
URL configuration for projectt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from register import views
from homepage import views
from checkout import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/' ,include("register.urls")),
    path('loginform/',include("loginform.urls")),
    path('',include("homepage.urls")),
    path('checkout/', include("checkout.urls")),
 
]
