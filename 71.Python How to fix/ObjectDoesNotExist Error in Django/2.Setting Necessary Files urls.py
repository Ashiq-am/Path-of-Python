from django.urls import path
from .views import get_book_by_title

urlpatterns = [
	path('books/<str:book_title>/', get_book_by_title,
		name='get_book_by_title'),
]
