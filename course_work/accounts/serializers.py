from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

    @staticmethod
    def validate_username(value):
        # Check for username uniqueness
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")

        # Check for invalid characters
        if not re.match(r'^[a-zA-Z0-9_.-]+$', value):
            raise serializers.ValidationError(
                "The username can only contain letters, numbers, dots, underscores, and hyphens."
            )

        return value

    @staticmethod
    def validate_email(value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    @staticmethod
    def validate_password(value):
        if len(value) < 8 or not any(c.isdigit() for c in value) or not any(c.isalpha() for c in value):
            raise serializers.ValidationError(
                "The password must be at least 8 characters long and include both letters and numbers."
            )
        return value
