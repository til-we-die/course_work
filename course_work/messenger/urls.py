from typing import List, Any
from django.urls import path
from .views import ChatRoomListCreateView, MessageListCreateView, UserChatRoomListView

urlpatterns: list[Any] = [
    path('api/chatrooms/', ChatRoomListCreateView.as_view(), name='chatroom-list-create'),
    path('api/chatrooms/<str:room_name>/messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('api/user/chatrooms/', UserChatRoomListView.as_view(), name='user-chatroom-list'),
]
