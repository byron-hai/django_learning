"""blog URL configuration"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', archive),
    url(r'^create/', create_blog_post),
    url(r'^signup/$', signup, name='signup'),
]
