from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^user/(?P<id>\d+)?/?$', views.UsersView, name='users'),
]

