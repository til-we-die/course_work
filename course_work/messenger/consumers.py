import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course_work.settings')
django.setup()

import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom
from .serializers import MessageSerializer


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        self.user = self.scope['user']

        print(f"Attempting to connect: user={self.user}, room_name={self.room_name}")
        try:
            self.room = await sync_to_async(ChatRoom.objects.get)(name=self.room_name)
            print(f"Room found: {self.room}")
        except ChatRoom.DoesNotExist:
            print("Room does not exist")
            await self.close()
            return

        # Проверка, является ли пользователь участником комнаты
        is_member = await sync_to_async(lambda: self.room.members.filter(id=self.user.id).exists())()
        print(f"Is user a member? {is_member}")
        if not is_member:
            print("User is not a member of the room")
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print("WebSocket connection accepted")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        from .models import Message
        data = json.loads(text_data)
        message_content = data.get('message', '').strip()
        if not message_content:
            return
        room = await sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        message = await sync_to_async(Message.objects.create)(room=room, user=self.user, content=message_content)
        message_data = MessageSerializer(message).data
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_data
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
