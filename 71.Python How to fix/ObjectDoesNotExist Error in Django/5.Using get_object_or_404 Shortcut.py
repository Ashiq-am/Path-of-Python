# views.py
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Book

def get_book_by_title(request, book_title):
	book = get_object_or_404(Book, title=book_title)
	return HttpResponse(f"The book {book.title} by {book.author} was found.")
