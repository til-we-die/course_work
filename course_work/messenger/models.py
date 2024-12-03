from django.contrib.auth.models import User
from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(User, related_name="chatrooms")

    def __str__(self):
        return self.name

    def get_display_name_for_user(self, user):
        other_members = self.members.exclude(id=user.id)
        if other_members.exists():
            return other_members.first().username
        return "Unknown"


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'
