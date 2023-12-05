from rest_framework import viewsets
from .serializers import RoomSerializers, MessageSerializers
from apps.core import models


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializers
    queryset = models.Room.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializers
    queryset = models.Message.objects.all()
