from django.urls import include, re_path, path
from . import views


urlpatterns = [
    re_path(r'tests/', views.demo, name='demo'),
    re_path(r'^(?P<revision>[\w\d\.-_]+)/(?P<prj_name>[\w\d\.-_]+)/$', views.tc_view, name='tc_view'),
]

