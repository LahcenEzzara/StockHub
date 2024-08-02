from django.urls import path
from . import views

app_name = "outgoing"

urlpatterns = [
    path('', views.outgoing, name='outgoing'),
    path('new/', views.new, name='new'),
    path('list/', views.outgoing, name='list'),
    path('graph/', views.graph, name='graph'),
]
