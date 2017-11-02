"""blog URL configuration"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page:': "/Successfully logged out/"}),
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^blog/create/$', create_blog, name="create"),
    url(r'^signup/$', signup, name='signup'),
    url(r'^learning/$', learn, name='learning'),
    url(r'^lifeeden/$', life_eden, name='lifeeden'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^about', about, name='about'),
]
