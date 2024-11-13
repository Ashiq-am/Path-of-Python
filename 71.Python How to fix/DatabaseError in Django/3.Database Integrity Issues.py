class MyModel(models.Model):
	name = models.CharField(max_length=50, unique=True)

# Attempt to create two instances with the same 'name'
try:
	instance1 = MyModel.objects.create(name='duplicate_name')
	instance2 = MyModel.objects.create(name='duplicate_name') # Causes DatabaseError
except IntegrityError as e:
	print(f"Database integrity issue: {e}")
