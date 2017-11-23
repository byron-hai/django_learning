""" URL configuration """
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', learning, name='learning'),
    url(r'^new/$', new_document, name="new"),
]
