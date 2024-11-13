from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import People

def get_people_by_name(request, name):
	try:
		people = People.objects.get(name=name)
		return HttpResponse(f"{people.name} and {people.age}")
	except ObjectDoesNotExist:
		return HttpResponse("Person not found.")
