"""Hoora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_register),
    path('image/',views.upload_image_user),
    path('get_home/',views.get_home),
    path('actions_set/',views.actions_set),
    path('delete_profile/',views.delete_profile),
    path('send_message/',views.send_message),
    path('get_matchs/',views.get_matchs),
    path('get_chat/',views.get_chat),
    path('get_profile/',views.get_profile)
] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
