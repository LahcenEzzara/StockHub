from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import MyUser

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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



def superuser_required(user):
    return user.is_authenticated and user.is_superuser


@login_required
def users(request):
    if not request.user.is_superuser:
        return redirect('index')
    return render(request, 'mgmt/users.html')


@login_required
def user_list(request):
    users = MyUser.objects.all()
    user_data = []

    for user in users:
        user_data.append({
            'name': user.get_full_name() or user.username,
            'username': user.username,
            'is_superuser': user.is_superuser,
            'email': user.email,
            'status': 'Active' if user.is_active else 'Inactive',
            'status_label': 'success' if user.is_active else 'danger',
            'avatar': user.avatar or 'https://cdn.jsdelivr.net/gh/LahcenEzzara/stockhub-cdn@main/img/avatars/1.png'
        })

    context = {
        'users': user_data
    }
    return render(request, 'mgmt/users.html', context)


@login_required
def user_detail(request, username):
    user = get_object_or_404(MyUser, username=username)
    return render(request, 'mgmt/user_detail.html', {'user': user})


@login_required
def new_user(request):
    if not request.user.is_superuser:
        return redirect('index')
    return render(request, 'mgmt/new_user.html')


@login_required
def settings(request):
    return render(request, 'mgmt/settings.html')

# def dev(request, number):
#     dev_number = number
#     return render(request, f'mgmt/dev_{dev_number}.html')


# Path: mgmt/urls.py
