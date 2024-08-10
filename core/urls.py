from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.users, name='users'),
    path('user/<id>', views.users_by_id, name='users_by_id'),
]

