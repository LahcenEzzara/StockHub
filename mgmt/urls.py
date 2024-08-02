from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),

    path('users/', views.users, name='users'),
    path('users/new/', views.new_user, name='new_user'),

    # path('under-maintenance/', views.under_maintenance, name='under_maintenance'),
    # path('page-under-maintenance/', views.page_under_maintenance,
    #      name='page_under_maintenance'),
]
