from django.urls import path
from . import views

app_name = "incoming"

urlpatterns = [
    path('', views.incoming, name='incoming'),
    path('new/', views.new, name='new'),
    path('list/', views.incoming, name='list'),
    path('graph/', views.graph, name='graph'),
]
