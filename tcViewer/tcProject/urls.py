from django.urls import include, re_path, path
from . import views


urlpatterns = [
    path(r'tcProjects/', views.testing_projects, name='tc_projects'),
    re_path(r'^(?P<revision>[\w\d\.-_]+)/(?P<prj_name>[\w\d\.-_]+)/$', views.tc_view, name='tc_view'),
]

