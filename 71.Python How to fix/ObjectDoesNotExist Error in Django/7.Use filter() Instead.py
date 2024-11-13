my_objects = MyModel.objects.filter(some_field=some_value)
if my_objects.exists():
	my_object = my_objects.first()
else:
	# Handle the case when no objects are found
	pass
