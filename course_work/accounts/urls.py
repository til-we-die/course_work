from django.urls import path
from .views import UserListCreate

urlpatterns = [
    path('api/users/', UserListCreate.as_view(), name='user-list-create'),
]
