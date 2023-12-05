from rest_framework import serializers
from apps.core import models


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'
