from rest_framework import serializers
from .models import UserProfile, Post
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio', 'friends']

    @staticmethod
    def get_friends(obj):
        friends = obj.friends.all()
        return [{"id": friend.user.id, "username": friend.user.username} for friend in friends]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']


class UserWithProfileSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'posts']


class AddFriendSerializer(serializers.Serializer):
    username = serializers.CharField()

    @staticmethod
    def validate_username(value):
        value = value.strip()
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким именем не найден.")
        return user
