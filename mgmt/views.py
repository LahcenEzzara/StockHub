from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            next_url = request.GET.get('next') or 'index'
            return redirect(next_url)
        else:
            error_message = "Invalid username or password."
            return render(request, 'mgmt/login.html', {'error_message': error_message})
    else:
        next_url = request.GET.get('next', '')
        return render(request, 'mgmt/login.html', {'next': next_url})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'mgmt/profile.html')


@login_required
def settings(request):
    return render(request, 'mgmt/settings.html')


def superuser_required(user):
    return user.is_authenticated and user.is_superuser


@login_required
def users(request):
    if not request.user.is_superuser:
        return redirect('index')
    return render(request, 'mgmt/users.html')


@login_required
def new_user(request):
    if not request.user.is_superuser:
        return redirect('index')
    return render(request, 'mgmt/new_user.html')


def under_maintenance(request):
    return render(request, 'mgmt/under_maintenance.html')


def page_under_maintenance(request):
    return render(request, 'mgmt/page_under_maintenance.html')

# Path: mgmt/urls.py
