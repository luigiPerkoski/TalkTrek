from rest_framework import serializers
from .models import *


class CoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields = ['id','username', 'email', 'online_status', 'is_active']


class RoomSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(queryset=CoreUser.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CoreUser.objects.all())

    class Meta:
        model = Room
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'