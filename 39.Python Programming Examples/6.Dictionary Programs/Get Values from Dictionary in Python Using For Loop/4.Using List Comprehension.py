# Dictionary
my_dict = {'name': 'Geeks', 'age': 20, 'city': 'India'}

# Using list comprehension
values = [my_dict[key] for key in my_dict]
for value in values:
	print(value)
