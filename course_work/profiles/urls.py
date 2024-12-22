from django.urls import path
from .views import UserProfileView, PostListCreateView, AddFriendView, SearchUserView, RemoveFriendView

urlpatterns = [
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/search-user/', SearchUserView.as_view(), name='search-user'),
    path('api/add-friend/', AddFriendView.as_view(), name='add-friend'),
    path('api/remove-friend/', RemoveFriendView.as_view(), name='remove-friend'),
]
