"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    #url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
]
