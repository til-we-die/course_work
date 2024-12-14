from django.urls import path
from .views import UserProfileView, PostListCreateView

urlpatterns = [
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
]
