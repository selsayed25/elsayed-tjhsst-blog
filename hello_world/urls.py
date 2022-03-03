from django.urls import path
from hello_world import views

url_patterns = [
    path('', views.hello_world, name = 'hello_world'),
]