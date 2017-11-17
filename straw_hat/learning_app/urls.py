""" URL configuration """
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^learning/$', learning, name='learning'),
    url(r'^learning/new/$', new_document, name="new"),
]
