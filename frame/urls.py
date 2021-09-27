from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login),
    path('redirect', views.redirect, name='redirect'),
]