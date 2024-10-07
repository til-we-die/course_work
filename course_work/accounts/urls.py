from django.urls import path

from accounts.views import logout_view, login_view, login_done_view, signup_view, signup_done_view

urlpatterns = [
    path('login/done/', login_done_view, name='login_done'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/done/', signup_done_view, name='signup_done'),
    path('signup/', signup_view, name='signup'),
]