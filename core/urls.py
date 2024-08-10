from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/<id>', views.users_by_id, name='users_by_id'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<id>', views.rooms_by_id, name='rooms_by_id'),
    path('messages/', views.messages, name='messages'),
    path('messages/<id>', views.messages_by_id, name='messages_by_id'),
]

