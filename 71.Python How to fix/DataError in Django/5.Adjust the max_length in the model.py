# models.py
from django.db import models

class MyModel(models.Model):
	name = models.CharField(max_length=20) # Adjust the maximum length according to your data requirements
