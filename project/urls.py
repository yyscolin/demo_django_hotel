"""Demo Django Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    Note: django.conf.urls.url() was deprecated in Django 3.0, and is removed
          in Django 4.0+.
"""
# from django.conf.urls import url (deprecated)
from django.urls import path
from django.contrib import admin
from home.views import home_view as home
from contact import views as contact
from rooms.views import rooms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax/contact/', contact.contact_ajax),
    path('contact/', contact.contact_view),
    path('rooms/', rooms),
    path('', home)
]
