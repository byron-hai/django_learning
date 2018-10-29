from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import auth_login, auth_logout
from django.urls import reverse_lazy
from . import views


urlpatterns = [
    url(r'^', views.dashboard, name='dashboard'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', auth_login, {'template_name': 'base.html'}, name='login'),
    url(r'^logout', auth_logout, {'next_page': reverse_lazy('dashboard')}, name='logout'),
    #url(r'^view/(?P<revision>[\w\d\.-_]+)/(?P<prj_name>[\w\d\.-_]+)/$', views.tc_view, name='tc_view'),
]
