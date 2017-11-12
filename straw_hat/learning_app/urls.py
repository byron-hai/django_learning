""" URL configuration """
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    url(r'^learning/$', learn, name='learning'),
    url(r'^learning/create/$', new_document, name="new"),
]
