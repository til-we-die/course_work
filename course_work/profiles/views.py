from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserWithProfileSerializer, AddFriendSerializer
from rest_framework import generics
from .models import Post, UserProfile
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework import status


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user
        serializer = UserWithProfileSerializer(user)
        return Response(serializer.data)


class SearchUserView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        username = request.query_params.get('username')
        if not username:
            return Response({"error": "Введите логин пользователя для поиска."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
            serializer = UserWithProfileSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)


class AddFriendView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = AddFriendSerializer(data=request.data)
        if serializer.is_valid():
            friend_user = serializer.validated_data['username']  # Объект User

            # Создаем профили, если их нет
            user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
            friend_profile, _ = UserProfile.objects.get_or_create(user=friend_user)

            if friend_profile in user_profile.friends.all():
                return Response(
                    {"message": "Пользователь уже в списке друзей."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_profile.friends.add(friend_profile)
            return Response(
                {"message": f"{friend_user.username} добавлен в друзья."},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveFriendView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = AddFriendSerializer(data=request.data)
        if serializer.is_valid():
            friend_user = serializer.validated_data['username']

            # Проверяем, есть ли профиль пользователя и друга
            try:
                user_profile = request.user.profile
                friend_profile = friend_user.profile
            except UserProfile.DoesNotExist:
                return Response(
                    {"error": "Профиль не найден."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Проверяем, является ли пользователь другом
            if friend_profile not in user_profile.friends.all():
                return Response(
                    {"message": "Пользователь не является другом."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_profile.friends.remove(friend_profile)
            return Response(
                {"message": f"{friend_user.username} удален из друзей."},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
