import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom, Message
from .serializers import MessageSerializer
from asgiref.sync import sync_to_async


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        self.user = self.scope['user']
        self.room = await sync_to_async(ChatRoom.objects.filter)(name=self.room_name)
        if not self.room.exists() or not await sync_to_async(
                lambda: self.room.first().members.filter(id=self.user.id).exists()
        )():
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
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
