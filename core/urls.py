from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_manager, name='users'),
]

