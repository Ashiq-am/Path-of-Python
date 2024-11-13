# models.py
from django.db import models

class UserProfile(models.Model):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(unique=True)
