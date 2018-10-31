from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'tests/', views.demo, name='demo'),
    #url(r'^view/(?P<revision>[\w\d\.-_]+)/(?P<prj_name>[\w\d\.-_]+)/$', views.tc_view, name='tc_view'),
]

