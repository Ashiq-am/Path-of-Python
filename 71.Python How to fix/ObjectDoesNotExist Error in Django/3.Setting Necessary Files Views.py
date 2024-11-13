#views.py
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Book

def get_book_by_title(request, book_title):
	book = Book.objects.get(title=book_title)
	return HttpResponse(f"The book {book.title} by {book.author} was found.")
