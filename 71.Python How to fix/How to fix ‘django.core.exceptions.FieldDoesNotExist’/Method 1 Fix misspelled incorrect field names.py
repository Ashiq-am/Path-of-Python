from django.db import models

class Product(models.Model):
	id = models.AutoField(primary_key=True) # It should be AutoField, not AutoField.
	name = models.CharField(max_length=100)
	price = models.IntegerField()

# Getting the product by using a non-existing field
# will lead to a field does not exist error.
# You should use 'filter' with the existing field 'price'.
obj = Product.objects.filter(price=1000)
