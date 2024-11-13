from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	message = models.TextField(max_length=500)
