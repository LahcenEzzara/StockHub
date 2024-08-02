from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),

    path('users/', views.user_list, name='users'),
    path('users/new/', views.new_user, name='new_user'),

    path('user/@<str:username>/', views.user_detail, name='user_detail'),

    # path('dev<int:number>/', views.dev, name='dev'),
]
