from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
