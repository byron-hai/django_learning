""" URL configuration"""
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', todo_today, name='todo_today'),
    url(r'^todo_today/$', todo_today, name='todo_today'),
    url(r'^todo_monthly/$', todo_monthly, name='todo_monthly'),
    url(r'^todo_yearly/$', todo_yearly, name='todo_yearly'),
]
