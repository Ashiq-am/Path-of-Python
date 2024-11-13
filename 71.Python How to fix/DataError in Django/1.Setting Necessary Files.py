# data_error_app/models.py
from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=1) # This intentionally causes a DataError
