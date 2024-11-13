# Incorrect: The field name is misspelled
my_object = MyModel.objects.get(some_filed=some_value)

# Correct: The field name is correct
my_object = MyModel.objects.get(some_field=some_value)
