from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from accounts.forms import RegisterForm


def login_view(request):
    return render(request, 'registration/login.html', {
        'form': AuthenticationForm,
    })


def logout_view(request):
    logout(request)
    return redirect('login')


def login_done_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile', username)
    else:
        return redirect('login')


def signup_view(request):
    return render(request, 'registration/signup.html', {
        'form': RegisterForm,
    })


def signup_done_view(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return render(request, 'registration/signup_done.html', {
            'username': user.username,
        })
    else:
        print(form.data)
        return redirect('signup')
