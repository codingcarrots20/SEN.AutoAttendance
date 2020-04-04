from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.loginView),
    path('scan/', views.scan),
    path('test/', views.test),
]