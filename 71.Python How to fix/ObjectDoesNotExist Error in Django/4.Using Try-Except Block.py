# views.py
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from .models import Book

def get_book_by_title(request, book_title):
	try:
		# Attempt to retrieve the book
		book = Book.objects.get(title=book_title)
		return HttpResponse(f"The book {book.title} by {book.author} was found.")
	except Book.DoesNotExist:
		# Handle the case where the book is not found
		raise Http404("The requested book does not exist.")
