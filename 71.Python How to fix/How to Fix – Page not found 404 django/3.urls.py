from django.contrib import admin
from django.urls import path, include

# Custom 404 error view
handler404 = 'views.error_404'
# Custom 500 error view
handler500 = 'views.error_500'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='home')
]
