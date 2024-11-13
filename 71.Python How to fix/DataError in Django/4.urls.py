from django.contrib import admin
from django.urls import path
from data_error_app.views import trigger_data_error

urlpatterns = [
	path('admin/', admin.site.urls),
	path('trigger_data_error/', trigger_data_error, name='trigger_data_error'),
]
