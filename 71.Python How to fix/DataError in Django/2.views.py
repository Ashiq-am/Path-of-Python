# data_error_app/views.py
from django.shortcuts import render
from django.db.utils import DataError
from .models import Person

def trigger_data_error(request):
	try:
		# This will trigger a DataError due to the length constraint on the 'name' field
		person = Person(name='John Doe')
		person.save()
	except DataError as e:
		# Handle the DataError here
		error_message = str(e)
		return render(request, 'trigger_data_error.html', {'error_message': error_message})
