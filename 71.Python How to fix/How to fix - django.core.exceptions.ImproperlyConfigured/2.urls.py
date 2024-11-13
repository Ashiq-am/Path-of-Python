# core/urls.py
from django.contrib import admin
from django.urls import include, path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

]
