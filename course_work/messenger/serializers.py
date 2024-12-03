from rest_framework import serializers
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatRoomSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'members', 'display_name']
        read_only_fields = ['name', 'members']

    def get_display_name(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.get_display_name_for_user(request.user)
        return "Unknown"


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'user', 'content', 'timestamp']
