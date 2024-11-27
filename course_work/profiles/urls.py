from django.urls import path
from .views import UserProfileView, PostListCreateView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
]
