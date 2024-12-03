from rest_framework import generics, permissions, serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import ChatRoom
from .serializers import MessageSerializer, ChatRoomSerializer
from django.contrib.auth.models import User


class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        recipient_username = self.request.data.get('recipient')

        try:
            recipient = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Recipient does not exist.")

        chat_room_name = f"{user.username}_{recipient.username}"
        chat_room = serializer.save(name=chat_room_name)

        chat_room.members.add(user)
        chat_room.members.add(recipient)


class MessageListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, room_name):
        room = get_object_or_404(ChatRoom, name=room_name)
        if not room.members.filter(id=request.user.id).exists():
            return Response({'error': 'Access denied'}, status=403)
        messages = room.messages.all().order_by('timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, room_name):
        room, created = ChatRoom.objects.get_or_create(name=room_name)
        if created:
            room.members.add(request.user)
        if not room.members.filter(id=request.user.id).exists():
            return Response({'error': 'Access denied'}, status=403)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(room=room, user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserChatRoomListView(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ChatRoom.objects.filter(members=user)
