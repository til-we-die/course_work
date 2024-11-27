from rest_framework import serializers
from .models import UserProfile, Post
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio']


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
