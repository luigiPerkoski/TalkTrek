from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('user', views.GetUsers, name='get_all_users'),
    path('user/<int:id>', views.GetUsersById, name='get_users_by_id'),
]
