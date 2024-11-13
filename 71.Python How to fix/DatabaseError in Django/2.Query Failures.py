try:
# Incorrect field name 'id'
	result = MyModel.objects.get(id=42)
except MyModel.DoesNotExist as e:
	print(f"Query failed: {e}")
