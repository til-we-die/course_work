from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


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

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Имя пользователя уже используется.")
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Введите корректный адрес электронной почты.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Электронная почта уже используется.")
        return value

    def validate_password(self, value):
        if len(value) < 8 or not any(c.isdigit() for c in value) or not any(c.isalpha() for c in value):
            raise serializers.ValidationError(
                "Пароль должен содержать минимум 8 символов, включать буквы и цифры."
            )
        return value