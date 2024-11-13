from django.db import models


class Car(models.Model):
	name = models.CharField()
	price = models.IntegerField()
	category = models.CharField() # newly added field
