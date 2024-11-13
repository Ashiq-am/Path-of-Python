from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import People

def get_people_by_name(request,name):
	people = People.objects.get(fullName=name)
	return HttpResponse(f"{people.name} and {people.age}")
