from django.urls import include, re_path, path
from . import views


urlpatterns = [
    path(r'projects/', views.testing_projects, name='tc_projects'),
    path(r'projects/create', views.create_new_project, name='create_project'),
    re_path(r'^reports/(?P<sw_revision>[\w\d.-]+)/$', views.tc_report, name='tc_report'),
    re_path(r'^(?P<sw_revision>[\w\d.-]+)/(?P<tc_name>[\w\d.-]+)/$', views.tc_view, name='tc_view'),
]
