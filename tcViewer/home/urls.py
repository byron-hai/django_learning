from django.urls import path, re_path
from django.contrib.auth.views import auth_login, auth_logout
from django.urls import reverse_lazy
from . import views


urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'signup/', views.signup, name='signup'),
    path(r'login/', views.user_login, name='login'),
    path(r'logout/', views.user_logout, name='logout'),
    path(r'dashboard/', views.get_sum_info, name='sum_info'),
    re_path(r'release_add/(?P<rel_type>[\w\d\._-]+)/$', views.release_add, name='release_add'),
    re_path(r'^sw_release/(?P<sw_revision>[\w\d.-]+)/new-testing-notes/$', views.create_testing_notes,
            name='create_tc_notes'),
]
