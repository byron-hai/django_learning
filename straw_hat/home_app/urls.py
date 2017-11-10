""" URL configuration"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^about/$', about, name='about'),
]
