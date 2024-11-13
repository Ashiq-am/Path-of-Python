from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import People

def get_people_by_name(request, name):
	try:
		# Utilize get_object_or_404 for a more robust query.
		people = get_object_or_404(People, name=name)
		return HttpResponse(f"{people.name} and {people.age}")
	except ObjectDoesNotExist:
		return HttpResponse("Person not found.")
