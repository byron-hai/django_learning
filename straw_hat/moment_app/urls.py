""" moment urls configuration  """
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    url(r'^$', moment, name='moment'),
    url(r'^new/$', keep_moment, name='new'),
]
