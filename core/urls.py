from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.users, name='users'),
    path('user/<id>', views.user_by_id, name='user_by_id'),
]

