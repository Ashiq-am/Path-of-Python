# Example: Enforcing unique constraint
class MyModel(models.Model):
	name = models.CharField(max_length=50, unique=True)

# Ensuring unique names
try:
	instance1 = MyModel.objects.create(name='unique_name')
	instance2 = MyModel.objects.create(name='unique_name') # Raises IntegrityError
except IntegrityError as e:
	print(f"Database integrity issue: {e}")
