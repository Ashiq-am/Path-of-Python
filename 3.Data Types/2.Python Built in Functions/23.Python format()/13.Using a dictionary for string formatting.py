introduction = 'My name is {first_name} {middle_name} {last_name} AKA the {aka}.'
full_name = {
	'first_name': 'Tony',
	'middle_name': 'Howard',
	'last_name': 'Stark',
	'aka': 'Iron Man',
}

# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))
