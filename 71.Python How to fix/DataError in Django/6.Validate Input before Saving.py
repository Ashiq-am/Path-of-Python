# views.py
from django.shortcuts import render
from .models import MyModel

def create_model_instance(request):
	try:
		name = 'ThisIsTooLongName'
		if len(name) <= MyModel._meta.get_field('name').max_length:
			MyModel.objects.create(name=name)
			message = 'Model instance created successfully.'
		else:
			message = 'Error: Name exceeds maximum length.'
	except Exception as e:
		message = f'Error: {e}'

	return render(request, 'index.html', {'message': message})
