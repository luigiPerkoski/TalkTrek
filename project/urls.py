from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.core.api.viewsets import MessageViewSet, RoomViewSet

route = DefaultRouter()
route.register('rooms', RoomViewSet, basename='rooms')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
