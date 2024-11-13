from django.urls import path
from . import views

url_pattern = [
path('register/', views.register, name='register'),]
