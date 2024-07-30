from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.GetUsers, name='get_all_users'),
]
