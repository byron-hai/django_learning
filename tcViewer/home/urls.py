from django.urls import path
from django.contrib.auth.views import auth_login, auth_logout
from django.urls import reverse_lazy
from . import views


urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'signup/', views.signup, name='signup'),
    path(r'login/', views.user_login, name='login'),
    path(r'logout', views.user_logout, name='logout'),
]
