from django.db import models

# Create your models here.
class People(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()