from .views import index, crud
from django.urls import path

urlpatterns = [
    path('', index.index, name='index'),
    path('room/<int:id>/', index.messages, name='message'),

]
