from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db import models

def home(request):
	return HttpResponse('Hello, World!')

def error_404(request, exception):
	print(hh)
	return render(request, 'templates/505_404.html', status=404)

def error_500(request):
	return render(request, 'templates/505_404.html', status=500)
